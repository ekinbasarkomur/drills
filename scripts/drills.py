"""What every script here shares: where a problem's files live, the plan, the solution region.

    LANGS                    rust, cpp, python (algorithms) and pandas, sql (the parallel tracks)
    path(file, lang)         leetcode/<lang>/.../<file>.<ext>
    files_for(id)            {lang: Path} of what exists in the repo for a LeetCode id
    load_plan()              plan.toml, flattened: one dict per problem, in solving order
    split(text, lang)        (above, solution, below) around the two marker lines
    is_stub(text, lang)      the solution still holds the scaffold's placeholder
"""
from __future__ import annotations

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LC = ROOT / "leetcode"

LANGS = {
    #          directory                   ext    comment  stub token in the solution region
    "rust":   (LC / "rust" / "src" / "bin", ".rs",  "//", "todo!()"),
    "cpp":    (LC / "cpp" / "solutions",    ".cpp", "//", "TODO()"),
    "python": (LC / "python",               ".py",  "#",  "raise NotImplementedError"),
    "pandas": (LC / "pandas",               ".py",  "#",  "raise NotImplementedError"),
    "sql":    (LC / "sql",                  ".sql", "--", "TODO: solve"),
}
ALGO_LANGS = ["rust", "cpp", "python"]
TRACK_LANGS = ["pandas", "sql"]
LABEL = {"rust": "Rust", "cpp": "C++", "python": "Python", "pandas": "Pandas", "sql": "SQL"}

# LeetCode's language slugs, as submissions report them, to ours.
FROM_LEETCODE = {"rust": "rust", "cpp": "cpp", "python3": "python", "python": "python",
                 "pythondata": "pandas", "mysql": "sql"}

DASH = "-" * 64


def marker(lang: str, which: str) -> str:
    return f"{LANGS[lang][2]} {DASH} {which}"


def path(file: str, lang: str) -> Path:
    d, ext, _, _ = LANGS[lang]
    return d / f"{file}{ext}"


def file_name(pid: int, slug: str) -> str:
    return f"lc{pid:04d}_{slug.replace('-', '_')}"


def files_for(pid: int) -> dict[str, Path]:
    out = {}
    for lang, (d, ext, _, _) in LANGS.items():
        hits = sorted(d.glob(f"lc{pid:04d}_*{ext}"))
        if hits:
            out[lang] = hits[0]
    return out


def all_files() -> dict[tuple[int, str], Path]:
    """Every problem file in the repo: {(id, lang): path}."""
    out = {}
    for lang, (d, ext, _, _) in LANGS.items():
        for p in sorted(d.glob(f"lc[0-9][0-9][0-9][0-9]_*{ext}")):
            out[(int(p.name[2:6]), lang)] = p
    return out


def load_plan() -> dict:
    """{"phases": [...], "tracks": [...], "problems": [flat list in order], "by_id": {id: problem}}.

    Each problem dict carries id, slug, file, tier?, why?, warmup? plus where it sits:
    kind ("phase" | "track"), phase (dict) and group (dict) or track (dict), langs, order."""
    raw = tomllib.loads((ROOT / "plan.toml").read_text())
    problems = []
    for ph in raw["phase"]:
        for g in ph["group"]:
            for p in g["problems"]:
                problems.append({**p, "kind": "phase", "phase": ph, "group": g, "langs": ALGO_LANGS})
    for t in raw.get("parallel", []):
        for p in t["problems"]:
            problems.append({**p, "kind": "track", "track": t, "langs": [t["lang"]]})
    for i, p in enumerate(problems):
        p["order"] = i
    return {"phases": raw["phase"], "tracks": raw.get("parallel", []), "problems": problems,
            "by_id": {p["id"]: p for p in problems}}


def plan_label(p: dict | None) -> str:
    if p is None:
        return "Plan dışı"
    if p["kind"] == "phase":
        return f"Aşama {p['phase']['id']} · {p['group']['name']}"
    return f"Paralel hat · {p['track']['name']}"


_MARK = re.compile(r"^(?://|#|--) -{8,} (solution|tests)\s*$", re.M)


def split(text: str, lang: str | None = None) -> tuple[str, str, str] | None:
    """(above, solution, below); `above` ends with the solution marker line, `below` starts
    with the tests marker line. None if the file has no markers."""
    marks = list(_MARK.finditer(text))
    sol = next((m for m in marks if m.group(1) == "solution"), None)
    tst = next((m for m in marks if m.group(1) == "tests" and sol and m.start() > sol.end()), None)
    if not sol or not tst:
        return None
    return text[: sol.end() + 1], text[sol.end() + 1: tst.start()], text[tst.start():]


def solution(text: str, lang: str | None = None) -> str:
    parts = split(text, lang)
    return parts[1] if parts else text


def is_stub(text: str, lang: str) -> bool:
    return LANGS[lang][3] in solution(text, lang)


def header_info(text: str) -> dict:
    """id, title, difficulty, url from the first header lines (old and new formats)."""
    head = "\n".join(text.splitlines()[:6])
    m = re.search(r"^(?://|#|--|\"\"\")?\s*(\d+)\.\s+(.+?)\s*(?:·\s*(Easy|Medium|Hard)\s*·\s*)?(https://\S+)?\s*$",
                  head, re.M)
    url = re.search(r"https://leetcode\.com/problems/[a-z0-9\-]+/", head)
    return {"id": int(m.group(1)) if m else None, "title": m.group(2).strip() if m else None,
            "difficulty": m.group(3) if m else None, "url": url.group(0) if url else None}
