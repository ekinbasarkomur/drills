"""Helpers for the pandas and SQL tests: build input tables, compare result tables.

    frame(columns, rows, types)        -> DataFrame with LeetCode's dtypes ({"col": "Int64",
                                          "day": "datetime64[ns]"}, from the problem's metadata)
    check(got, columns, rows, ordered) -> assert like LeetCode's judge: same column names,
                                          same rows (in any order unless the problem says
                                          "ordered by"), numbers compared to 1e-5, null = NaN/None

check always prints the table the solution returned, and on a mismatch prints what
was wanted next to it and names the rows that differ. Printing needs pytest's
capture off; `make <id>` and `make pandas-<id>` already pass -s.
"""
import math
import os

import pandas as pd


def frame(columns, rows, types=None):
    df = pd.DataFrame(rows, columns=columns)
    for col, t in (types or {}).items():
        if col not in df:
            continue
        low = t.lower()
        try:
            if low.startswith(("datetime", "date", "timestamp")):
                df[col] = pd.to_datetime(df[col])
            elif low not in ("object", "varchar", "text"):
                df[col] = df[col].astype(t)
        except (TypeError, ValueError):
            pass
    return df


def _cell(v):
    try:
        if v is None or pd.isna(v):
            return None
    except (TypeError, ValueError):
        pass
    if hasattr(v, "strftime"):
        return v.strftime("%Y-%m-%d") if getattr(v, "hour", 0) == 0 and getattr(v, "minute", 0) == 0 else str(v)
    if isinstance(v, bool):
        return str(v).lower()
    try:
        f = float(v)
        if math.isfinite(f) and not (isinstance(v, str) and not v.strip().lstrip("-").replace(".", "", 1).isdigit()):
            return round(f, 5)
    except (TypeError, ValueError):
        pass
    return str(v)


def _norm_rows(rows):
    return [tuple(_cell(v) for v in r) for r in rows]


def _case():
    """The name of the test being run, for the heading above each printed table."""
    current = os.environ.get("PYTEST_CURRENT_TEST", "")
    return current.split("::")[-1].split(" ")[0] or "check"


def _text(v):
    """How a cell is shown. _cell has already turned every number into a float,
    so a whole one is printed without its .0, the way LeetCode prints it."""
    if v is None:
        return "null"
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def _table(columns, rows, indent="  "):
    """The rows as an aligned text table, the way LeetCode prints one."""
    head = [str(c) for c in columns]
    body = [[_text(v) for v in r] for r in rows]
    width = [max([len(h)] + [len(r[i]) for r in body]) for i, h in enumerate(head)]
    line = indent + "  ".join(h.ljust(w) for h, w in zip(head, width))
    rule = indent + "  ".join("-" * w for w in width)
    out = [line, rule]
    out += [indent + "  ".join(c.ljust(w) for c, w in zip(r, width)) for r in body] or [indent + "(no rows)"]
    return "\n".join(out)


def check(got, columns, rows, ordered=False):
    __tracebackhide__ = True  # point the failure at the test, not at this file
    case = _case()
    print(f"\n--- {case} " + "-" * max(3, 68 - len(case)))

    if not isinstance(got, pd.DataFrame):
        print(f"  returned {got!r}, which is a {type(got).__name__}, not a DataFrame")
        raise AssertionError(
            f"{case}: expected a DataFrame, got {type(got).__name__}\n\nwanted:\n"
            + _table(columns, _norm_rows(rows))
        )

    g = _norm_rows(got.astype(object).itertuples(index=False, name=None))
    print(_table(got.columns, g))

    if list(got.columns) != list(columns):
        raise AssertionError(
            f"{case}: wrong columns\n\n  got:    {list(got.columns)}\n  wanted: {list(columns)}"
        )

    w = _norm_rows(rows)
    if not ordered:
        g, w = sorted(g, key=repr), sorted(w, key=repr)
    if g == w:
        return

    parts = ["got:\n" + _table(columns, g), "wanted:\n" + _table(columns, w)]
    missing = _dedupe([r for r in w if g.count(r) < w.count(r)])
    extra = _dedupe([r for r in g if w.count(r) < g.count(r)])
    if missing:
        parts.append("rows that never came:\n" + _table(columns, missing))
    if extra:
        parts.append("rows that should not be there:\n" + _table(columns, extra))
    if not missing and not extra:
        parts.append("the rows are right but in the wrong order, and this problem is ordered")
    raise AssertionError(f"{case}: wrong table\n\n" + "\n\n".join(parts))


def _dedupe(rows):
    seen, out = set(), []
    for r in rows:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out
