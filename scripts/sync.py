#!/usr/bin/env python3
"""Write accepted LeetCode submissions into the problem files, test them, commit.

Called by the Obsidian vault's leetcode_sync.py with a JSON list on stdin:

    [{"id": 146, "lang": "rust", "code": "...", "submission_id": "123", "timestamp": 1700000000}, ...]

`lang` is LeetCode's slug (rust, cpp, python3, python, pythondata, mysql). For each
(problem, language) only the newest submission counts, and it is written only when

  - it is newer than what the file holds: newer than the last submission synced into it
    (.cache/synced.json), or, with no record, newer than the file's last commit; a file that
    still holds the scaffold's stub always takes it;
  - the file has no uncommitted changes (`git status --porcelain <file>`): local work wins;
  - its code differs from the file's solution.

--force drops the first rule: the newest accepted submission is written even when it is
older than the file's last commit or the last synced one (e.g. after a restructure commit).
Uncommitted local changes still win, and every written submission is recorded as usual.

Only the solution region (between the two marker lines) is replaced; the header and the
tests stay. A missing file is scaffolded with scripts/new.py first. Each written file's
tests are run in that language; a submission that fails them is not written (the file goes
back to what it was and the problem is listed as skipped). One commit holds the rest
("LeetCode sync: 146 rust, 23 cpp"). Nothing is pushed.

    scripts/sync.py [--dry-run] [--no-commit] [--force] < submissions.json

Prints a JSON report: {"written": [...], "skipped": [...], "commit": sha | null}.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drills import FROM_LEETCODE, LABEL, ROOT, files_for, is_stub, split  # noqa: E402

RECORD = ROOT / ".cache" / "synced.json"


def git(*args, check=False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=check)


def last_commit_time(path: Path) -> int | None:
    out = git("log", "-1", "--format=%ct", "--", str(path.relative_to(ROOT))).stdout.strip()
    return int(out) if out else None


def dirty(path: Path) -> bool:
    return bool(git("status", "--porcelain", "--", str(path.relative_to(ROOT))).stdout.strip())


def clean_code(code: str, above: str, lang: str) -> str:
    code = code.replace("\r\n", "\n").strip("\n") + "\n"
    if lang == "rust":
        # A `use` that is already above the region would be imported twice: an error.
        have = {l.strip() for l in above.splitlines() if l.strip().startswith("use ")}
        code = "\n".join(l for l in code.split("\n") if l.strip() not in have).lstrip("\n")
        code = re.sub(r"(?m)^\s*(pub )?struct Solution\s*;\s*\n", "", code) if "struct Solution;" in above else code
    return code


def same(a: str, b: str) -> bool:
    return [l.rstrip() for l in a.strip().splitlines()] == [l.rstrip() for l in b.strip().splitlines()]


def ensure_file(pid: int, lang: str) -> Path | None:
    p = files_for(pid).get(lang)
    if p:
        return p
    subprocess.run([sys.executable, str(ROOT / "scripts" / "new.py"), str(pid), "--lang", lang],
                   cwd=ROOT, capture_output=True, text=True)
    return files_for(pid).get(lang)


def run_tests(pid: int, lang: str) -> bool:
    o = subprocess.run([sys.executable, str(ROOT / "scripts" / "run.py"), str(pid), "--lang", lang],
                       cwd=ROOT, capture_output=True, text=True)
    return o.returncode == 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report what would be written, touch nothing")
    ap.add_argument("--no-commit", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="write the newest submission even if it is older than the file (local changes still win)")
    args = ap.parse_args()
    subs = json.load(sys.stdin)
    record = json.loads(RECORD.read_text()) if RECORD.exists() else {}

    newest: dict[tuple[int, str], dict] = {}
    for s in subs:
        lang = FROM_LEETCODE.get(s.get("lang", ""))
        if not lang:
            continue
        key = (int(s["id"]), lang)
        if key not in newest or int(s["timestamp"]) > int(newest[key]["timestamp"]):
            newest[key] = s

    written, skipped, created = [], [], []
    for (pid, lang), s in sorted(newest.items()):
        ts = int(s["timestamp"])
        existed = files_for(pid).get(lang)
        if existed is None and args.dry_run:
            written.append({"id": pid, "lang": lang, "file": None, "new_file": True, "submission": s["submission_id"]})
            continue
        path = existed or ensure_file(pid, lang)
        if path is None:
            skipped.append({"id": pid, "lang": lang, "why": "could not scaffold the file"})
            continue
        rel = str(path.relative_to(ROOT))
        if existed is None:
            created.append(rel)
        text = path.read_text()
        parts = split(text)
        if parts is None:
            skipped.append({"id": pid, "lang": lang, "file": rel, "why": "no solution/tests marker lines"})
            continue
        above, region, below = parts
        if existed is not None and dirty(path):
            skipped.append({"id": pid, "lang": lang, "file": rel, "why": "uncommitted local changes"})
            continue
        rec = record.get(rel)
        stub = is_stub(text, lang)
        held = rec and (str(rec["submission"]) == str(s["submission_id"]) if args.force else int(rec["timestamp"]) >= ts)
        if held:
            skipped.append({"id": pid, "lang": lang, "file": rel, "why": "already holds this or a newer submission"})
            continue
        if not rec and not stub and not args.force:
            committed = last_commit_time(path)
            if committed and committed > ts:
                skipped.append({"id": pid, "lang": lang, "file": rel,
                                "why": "the file was committed after this submission (local code is newer)"})
                continue
        code = clean_code(s["code"], above, lang)
        if same(code, region):
            record[rel] = {"submission": str(s["submission_id"]), "timestamp": ts}
            skipped.append({"id": pid, "lang": lang, "file": rel, "why": "already identical"})
            continue
        if args.dry_run:
            written.append({"id": pid, "lang": lang, "file": rel, "submission": s["submission_id"], "dry_run": True})
            continue
        original = path.read_text()
        path.write_text(above + code + below)
        if not run_tests(pid, lang):  # e.g. a class wrapper the repo's tests don't call: keep what works
            path.write_text(original)
            skipped.append({"id": pid, "lang": lang, "file": rel,
                            "why": "the submission fails this file's tests; the file was left as it was"})
            continue
        record[rel] = {"submission": str(s["submission_id"]), "timestamp": ts}
        written.append({"id": pid, "lang": lang, "file": rel, "submission": s["submission_id"], "tests_pass": True})

    commit = None
    if not args.dry_run:
        RECORD.parent.mkdir(parents=True, exist_ok=True)
        RECORD.write_text(json.dumps(record, indent=1, sort_keys=True))
        if written and not args.no_commit:
            files = [w["file"] for w in written]
            git("add", "--", *files, check=True)
            msg = "LeetCode sync: " + ", ".join(f"{w['id']} {w['lang']}" for w in written)
            body = "\n".join(f"- {w['id']} {LABEL[w['lang']]}: submission {w['submission']}, tests "
                             f"{'pass' if w['tests_pass'] else 'FAIL'}" for w in written)
            r = git("commit", "-m", msg, "-m", body, "--", *files)
            if r.returncode == 0:
                commit = git("rev-parse", "--short", "HEAD").stdout.strip()
    for c in created:  # scaffolded for a submission that was then not written: leave no stray file
        if not any(w.get("file") == c for w in written):
            (ROOT / c).unlink(missing_ok=True)
    print(json.dumps({"written": written, "skipped": skipped, "commit": commit}, indent=1))


if __name__ == "__main__":
    main()
