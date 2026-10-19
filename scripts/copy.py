#!/usr/bin/env python3
"""Copy a problem's solution (the part between the two marker lines) to the clipboard,
ready to paste into LeetCode's editor.

    scripts/copy.py 146 rust        rust, cpp, python, pandas or sql
    scripts/copy.py 146             the only language that has one, or the only one solved
    scripts/copy.py 146 rust --print   print it instead
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drills import LANGS, ROOT, files_for, is_stub, solution  # noqa: E402

ALIASES = {"py": "python", "c++": "cpp", "rs": "rust", "mysql": "sql", "pd": "pandas"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("id", type=int)
    ap.add_argument("lang", nargs="?")
    ap.add_argument("--print", action="store_true")
    args = ap.parse_args()
    files = files_for(args.id)
    if not files:
        sys.exit(f"no file for {args.id}")
    lang = ALIASES.get((args.lang or "").lower(), (args.lang or "").lower()) or None
    if lang is None:
        solved = [l for l, p in files.items() if not is_stub(p.read_text(), l)]
        pick = list(files) if len(files) == 1 else solved
        if len(pick) != 1:
            sys.exit(f"which language? {args.id} has: {', '.join(files)}  (make copy {args.id} rust)")
        lang = pick[0]
    if lang not in LANGS or lang not in files:
        sys.exit(f"{args.id} has no {lang} file; it has: {', '.join(files)}")
    text = files[lang].read_text()
    code = solution(text, lang).strip("\n") + "\n"
    if lang == "sql":  # the scaffold's own marker line is not part of the answer
        code = "\n".join(l for l in code.splitlines() if "TODO: solve" not in l) + "\n"
    if args.print:
        print(code, end="")
        return
    subprocess.run(["pbcopy"], input=code, text=True, check=True)
    note = "  (still the unsolved stub)" if is_stub(text, lang) else ""
    print(f"copied {len(code.splitlines())} lines of {files[lang].relative_to(ROOT)} to the clipboard{note}")


if __name__ == "__main__":
    main()
