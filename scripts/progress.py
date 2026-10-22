#!/usr/bin/env python3
"""What is solved in which language, by running the tests.

    scripts/progress.py                 summary per plan group, plus anything in progress
    scripts/progress.py -v              every problem, one row each
    scripts/progress.py 146 1           only these problems
    scripts/progress.py --write         also rewrite PROGRESS.md
    scripts/progress.py --next          the next problem to solve, per language and track
    scripts/progress.py --json          machine-readable status (the Obsidian sync reads it)
    scripts/progress.py --verify-stubs  run the unsolved stubs too and report any that pass

Solved = the scaffold's stub is gone from the solution AND the file's tests pass. Stub files
are never run. Results are cached in .cache/status.json by file content (plus the shared
helpers of that language), so only what changed since the last run is tested again.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import leetcode  # noqa: E402
from drills import (ALGO_LANGS, LABEL, LANGS, LC, ROOT, all_files, header_info, is_stub,  # noqa: E402
                    load_plan)

CACHE = ROOT / ".cache" / "status.json"
HELPERS = {
    "rust": [LC / "rust/Cargo.toml", LC / "rust/src/lib.rs"],
    "cpp": sorted((LC / "cpp/include").glob("*.hpp")) + [LC / "cpp/Makefile"],
    "python": [LC / "python/_lc.py", LC / "python/list_node.py", LC / "python/tree_node.py", LC / "pyproject.toml"],
    "pandas": [LC / "python/_pd.py", LC / "pyproject.toml"],
    "sql": [LC / "python/_pd.py", LC / "sql/conftest.py", LC / "pyproject.toml"],
}
TIMEOUT = 900


def digest(path: Path, lang: str) -> str:
    h = hashlib.sha256(path.read_bytes())
    for f in HELPERS[lang]:
        if f.exists():
            h.update(f.read_bytes())
    return h.hexdigest()


# ---------------------------------------------------------------- runners: [Path] -> {Path: ok}

def run_rust(paths):
    """Compile them all (a binary that does not compile counts as failing), then one cargo test."""
    if not paths:
        return {}
    res = {p: False for p in paths}
    by_stem = {p.stem: p for p in paths}
    bins = lambda ps: [a for p in ps for a in ("--bin", p.stem)]
    b = subprocess.run(["cargo", "build", "--tests", "--keep-going"] + bins(paths), cwd=LC / "rust",
                       capture_output=True, text=True, timeout=TIMEOUT)
    broken = set(re.findall(r'could not compile `leetcode` \(bin "(\w+)" test\)', b.stderr))
    if b.returncode != 0 and not broken:  # something else is wrong (the library, Cargo.toml)
        return res
    good = [p for p in paths if p.stem not in broken]
    if not good:
        return res
    o = subprocess.run(["cargo", "test", "--no-fail-fast"] + bins(good), cwd=LC / "rust",
                       capture_output=True, text=True, timeout=TIMEOUT)
    # stderr names each binary as it starts ("Running unittests src/bin/<stem>.rs"), stdout has
    # its "test result" line; both come out in the same order.
    names = re.findall(r"Running unittests src/bin/(\w+)\.rs", o.stderr)
    results = re.findall(r"^test result: (ok|FAILED)\.", o.stdout, re.M)
    if len(names) == len(results) == len(good):
        for n, r in zip(names, results):
            res[by_stem[n]] = r == "ok"
        return res
    for p in good:  # could not pair them up: one binary at a time
        o = subprocess.run(["cargo", "test", "--bin", p.stem], cwd=LC / "rust",
                           capture_output=True, text=True, timeout=TIMEOUT)
        res[p] = o.returncode == 0 and "test result: ok" in o.stdout
    return res


def run_cpp(paths):
    if not paths:
        return {}
    for p in paths:  # a stale binary from an older version must not count
        (LC / "cpp" / "build" / p.stem).unlink(missing_ok=True)
    subprocess.run(["make", "--no-print-directory", "-k", "-j8"] + [f"build/{p.stem}" for p in paths],
                   cwd=LC / "cpp", capture_output=True, text=True, timeout=TIMEOUT)
    res = {}
    for p in paths:
        exe = LC / "cpp" / "build" / p.stem
        if not exe.exists():
            res[p] = False
            continue
        try:
            o = subprocess.run([str(exe)], capture_output=True, text=True, timeout=60)
            res[p] = o.returncode == 0 and "test result: ok" in o.stdout
        except subprocess.TimeoutExpired:
            res[p] = False
    return res


def run_pytest(paths):
    if not paths:
        return {}
    rel = [str(p.relative_to(ROOT)) for p in paths]
    o = subprocess.run(["uv", "run", "--quiet", "pytest", "-q", "--tb=no", "-rA", "--continue-on-collection-errors", *rel], cwd=ROOT,
                       capture_output=True, text=True, timeout=TIMEOUT)
    if o.returncode not in (0, 1, 5):  # 2+ = interrupted, internal error, usage error
        return {p: False for p in paths}
    bad = {m.group(2) for m in re.finditer(r"^(FAILED|ERROR) ([^\s:]+)", o.stdout, re.M)}
    return {p: str(p.relative_to(LC)) not in bad for p in paths}


RUNNERS = {"rust": run_rust, "cpp": run_cpp, "python": run_pytest, "pandas": run_pytest, "sql": run_pytest}


# ---------------------------------------------------------------- status

def status(only: set[int] | None = None, verify_stubs: bool = False) -> dict[tuple[int, str], str]:
    """{(id, lang): "solved" | "failing" | "stub"} for every problem file in the repo."""
    files = {k: v for k, v in all_files().items() if not only or k[0] in only}
    try:
        cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    except ValueError:
        cache = {}
    out, todo = {}, {"rust": [], "cpp": [], "py": []}
    for (pid, lang), path in files.items():
        stub = is_stub(path.read_text(), lang)
        if stub and not verify_stubs:
            out[(pid, lang)] = "stub"
            continue
        key = str(path.relative_to(ROOT))
        h = digest(path, lang)
        if not stub and cache.get(key, {}).get("hash") == h:
            out[(pid, lang)] = "solved" if cache[key]["ok"] else "failing"
            continue
        todo["py" if lang in ("python", "pandas", "sql") else lang].append(((pid, lang), path, h, key, stub))
    for kind, batch in todo.items():
        if not batch:
            continue
        try:
            res = RUNNERS["python" if kind == "py" else kind]([j[1] for j in batch])
        except subprocess.TimeoutExpired:  # an endless loop somewhere: none of this batch counts
            print(f"  {kind}: tests did not finish in {TIMEOUT}s, counted as failing", file=sys.stderr)
            res = {}
        for k, path, h, key, stub in batch:
            ok = res.get(path, False)
            if stub:
                out[k] = "STUB PASSES" if ok else "stub"
                continue
            out[k] = "solved" if ok else "failing"
            cache[key] = {"hash": h, "ok": ok}
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))
    return out


# ---------------------------------------------------------------- output

def tick(s: str | None) -> str:
    return "—" if s is None else "✅" if s == "solved" else "▢"


def title_of(pid: int, path: Path | None) -> tuple[str, str, str]:
    """title, difficulty, url: from the cached LeetCode data when there is some, else the header."""
    info = header_info(path.read_text()) if path else {"title": None, "difficulty": None, "url": None}
    slug = re.search(r"problems/([a-z0-9\-]+)/", info["url"] or "")
    if slug and (leetcode.CACHE / f"{slug.group(1)}.json").exists():
        q = json.loads((leetcode.CACHE / f"{slug.group(1)}.json").read_text())
        return q["title"], q["difficulty"], info["url"]
    return info["title"] or "?", info["difficulty"] or "", info["url"] or ""


def counts(st, ps, langs):
    return {l: (sum(st.get((p["id"], l)) == "solved" for p in ps), sum((p["id"], l) in st for p in ps)) for l in langs}


def fmt(c):
    return "   ".join(f"{LABEL[l].lower():<6} {a:>3}/{b:<3}" for l, (a, b) in c.items())


def summary(plan, st, verbose: bool):
    for ph in plan["phases"]:
        print(f"\nAşama {ph['id']} · {ph['name']}")
        for g in ph["group"]:
            ps = [p for p in plan["problems"] if p["kind"] == "phase" and p["group"] is g]
            print(f"  {g['name']:<34} {fmt(counts(st, ps, ALGO_LANGS))}")
            if verbose:
                for p in ps:
                    print(f"      {p['id']:>5}  {p['file']:<62}" + "  ".join(tick(st.get((p['id'], l))) for l in ALGO_LANGS))
    print("\nParalel hat")
    for t in plan["tracks"]:
        ps = [p for p in plan["problems"] if p["kind"] == "track" and p["track"] is t]
        print(f"  {t['name']:<34} {fmt(counts(st, ps, [t['lang']]))}")
        if verbose:
            for p in ps:
                print(f"      {p['id']:>5}  {p['file']:<62}{tick(st.get((p['id'], t['lang'])))}")
    algo = [p for p in plan["problems"] if p["kind"] == "phase"]
    print(f"\n  {'plan total':<34} {fmt(counts(st, algo, ALGO_LANGS))}")
    extra = sorted({pid for pid, _ in st} - set(plan["by_id"]))
    if extra:
        print(f"  {'outside the plan':<34} " + ", ".join(
            f"{pid} (" + " ".join(f"{l} {tick(st[(pid, l)])}" for l in LANGS if (pid, l) in st) + ")" for pid in extra))
    failing = sorted(k for k, v in st.items() if v == "failing")
    if failing:
        print("\n  in progress (stub removed, tests not passing yet): "
              + ", ".join(f"{pid} {lang}" for pid, lang in failing))
    bad = sorted(k for k, v in st.items() if v == "STUB PASSES")
    if bad:
        print("\n  STUBS THAT PASS THEIR TESTS: " + ", ".join(f"{pid} {lang}" for pid, lang in bad))


def next_up(plan, st):
    for lang in ALGO_LANGS:
        p = next((p for p in plan["problems"] if p["kind"] == "phase" and (p["id"], lang) in st
                  and st[(p["id"], lang)] != "solved"), None)
        if p:
            short = "py" if lang == "python" else lang
            print(f"  {LABEL[lang]:<7} {p['id']:>5}  {p['file']:<58} Aşama {p['phase']['id']} · "
                  f"{p['group']['name']:<30} make {short}-{p['id']}")
        else:
            print(f"  {LABEL[lang]:<7} every plan problem is solved")
    for t in plan["tracks"]:
        p = next((p for p in plan["problems"] if p["kind"] == "track" and p["track"] is t
                  and st.get((p["id"], t["lang"])) != "solved"), None)
        if p:
            print(f"  {t['name']:<7} {p['id']:>5}  {p['file']:<58} {'Paralel hat':<40} make {t['lang']}-{p['id']}")


def write_progress(plan, st):
    files = all_files()
    first = {}
    for (pid, _lang), p in files.items():
        first.setdefault(pid, p)
    algo = [p for p in plan["problems"] if p["kind"] == "phase"]
    tot = counts(st, algo, ALGO_LANGS)
    track_tot = [(t, sum(st.get((p["id"], t["lang"])) == "solved" for p in t["problems"])) for t in plan["tracks"]]
    out = ["# Progress", "",
           "Generated by `make progress` from [`plan.toml`](plan.toml) and the tests. ✅ = the stub is gone",
           "and the file's tests pass, ▢ = not yet, — = no file in that language. Phases are solved",
           "in order, groups top to bottom; the parallel tracks run alongside, one problem a day.",
           "*ısınma* = a warm-up the researched plan did not list, the prerequisite of the next problem.",
           "", "**" + " &nbsp;·&nbsp; ".join([f"{LABEL[l]} {a}/{len(algo)}" for l, (a, _) in tot.items()]
                                          + [f"{t['name']} {d}/{len(t['problems'])}" for t, d in track_tot]) + "**"]

    def row(p, langs, n):
        title, diff, url = title_of(p["id"], first.get(p["id"]))
        warm = " *(ısınma)*" if p.get("warmup") else ""
        cells = " | ".join(tick(st.get((p["id"], l))) for l in langs)
        return f"| {n} | [{p['id']}]({url}) | {title}{warm} | {diff} | {cells} | `{p['file']}` |"

    n = 0
    for ph in plan["phases"]:
        ps = [p for p in algo if p["phase"] is ph]
        out += ["", f"## Aşama {ph['id']} · {ph['name']}", "", ph["why"], "",
                "<sub>" + " · ".join(f"{LABEL[l]} {a}/{b}" for l, (a, b) in counts(st, ps, ALGO_LANGS).items()) + "</sub>"]
        for g in ph["group"]:
            out += ["", f"### {g['name']}", ""] + ([g["why"], ""] if g.get("why") else [])
            out += ["| # | No | Problem | Difficulty | Rust | C++ | Python | File |",
                    "| ---: | ---: | --- | --- | :---: | :---: | :---: | --- |"]
            for p in ps:
                if p["group"] is g:
                    n += 1
                    out.append(row(p, ALGO_LANGS, n))
    out += ["", "## Paralel hat"]
    for t, done in track_tot:
        ps = [q for q in plan["problems"] if q["kind"] == "track" and q["track"] is t]
        out += ["", f"### {t['name']}", "", t["why"], "", f"<sub>{done}/{len(ps)}</sub>", "",
                f"| # | No | Problem | Difficulty | {LABEL[t['lang']]} | File |", "| ---: | ---: | --- | --- | :---: | --- |"]
        days = any("day" in p for p in ps)  # a study plan with days and sections (30 Days of Pandas)
        if days:
            out[-2:] = [f"| Day | No | Problem | Difficulty | {LABEL[t['lang']]} | File | Section |",
                        "| ---: | ---: | --- | --- | :---: | --- | --- |"]
        out += [row(p, [t["lang"]], p["day"]) + f" {p.get('section', '')} |" if days else row(p, [t["lang"]], i)
                for i, p in enumerate(ps, 1)]
    extra = sorted({pid for pid, _ in st} - set(plan["by_id"]))
    if extra:
        out += ["", "## Plan dışı", "", "In the repo but not in the plan.", "",
                "| No | Problem | Difficulty | Rust | C++ | Python | Pandas | SQL | File |",
                "| ---: | --- | --- | :---: | :---: | :---: | :---: | :---: | --- |"]
        for pid in extra:
            title, diff, url = title_of(pid, first[pid])
            out.append(f"| [{pid}]({url}) | {title} | {diff} | " + " | ".join(tick(st.get((pid, l))) for l in LANGS)
                       + f" | `{first[pid].stem}` |")
    (ROOT / "PROGRESS.md").write_text("\n".join(out) + "\n")
    print(f"\nwrote PROGRESS.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="*", type=int)
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--next", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verify-stubs", action="store_true")
    args = ap.parse_args()
    plan = load_plan()
    st = status(set(args.ids) or None, verify_stubs=args.verify_stubs)
    if args.json:
        files = all_files()
        out = {}
        for (pid, lang), s in st.items():
            out.setdefault(str(pid), {})[lang] = {"status": s, "path": str(files[(pid, lang)].relative_to(ROOT))}
        print(json.dumps(out, indent=1, sort_keys=True))
    elif args.next:
        next_up(plan, st)
    elif args.ids:
        for (pid, lang), s in sorted(st.items()):
            print(f"  {pid:>5} {lang:<7} {s}")
    else:
        summary(plan, st, args.verbose)
        if args.write:
            write_progress(plan, st)


if __name__ == "__main__":
    main()
