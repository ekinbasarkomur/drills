#!/usr/bin/env python3
"""Run one problem's tests, in every language it has (or one), with the full output.

    scripts/run.py 146              rust, cpp, python (or pandas / sql) in turn
    scripts/run.py 146 --lang rust  only that one
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drills import LABEL, LANGS, LC, ROOT, files_for, is_stub  # noqa: E402


def command(lang: str, path: Path) -> tuple[list[str], Path]:
    if lang == "rust":
        return ["cargo", "test", "--quiet", "--bin", path.stem], LC / "rust"
    if lang == "cpp":
        return ["make", "--no-print-directory", path.stem], LC / "cpp"
    return ["uv", "run", "--quiet", "pytest", "-q", str(path.relative_to(LC))], LC


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("id", type=int)
    ap.add_argument("--lang", choices=list(LANGS))
    args = ap.parse_args()
    files = files_for(args.id)
    if args.lang:
        files = {k: v for k, v in files.items() if k == args.lang}
    if not files:
        sys.exit(f"no {args.lang + ' ' if args.lang else ''}file for {args.id}; `make new {args.id}` scaffolds one")
    summary, failed = [], False
    for lang, path in files.items():
        print(f"\n== {LABEL[lang]} · {path.relative_to(ROOT)}", flush=True)
        cmd, cwd = command(lang, path)
        ok = subprocess.run(cmd, cwd=cwd).returncode == 0
        stub = is_stub(path.read_text(), lang)
        failed |= not ok
        summary.append(f"{LABEL[lang].lower()} {'ok' if ok and not stub else 'stub (not solved yet)' if stub else 'FAILED'}")
    print("\n" + " · ".join(summary))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
