"""Helpers for the pandas and SQL tests: build input tables, compare result tables.

    frame(columns, rows, types)        -> DataFrame with LeetCode's dtypes ({"col": "Int64",
                                          "day": "datetime64[ns]"}, from the problem's metadata)
    check(got, columns, rows, ordered) -> assert like LeetCode's judge: same column names,
                                          same rows (in any order unless the problem says
                                          "ordered by"), numbers compared to 1e-5, null = NaN/None
"""
import math

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


def check(got, columns, rows, ordered=False):
    assert isinstance(got, pd.DataFrame), f"expected a DataFrame, got {type(got).__name__}"
    assert list(got.columns) == list(columns), f"columns {list(got.columns)} != {list(columns)}"
    g = _norm_rows(got.astype(object).itertuples(index=False, name=None))
    w = _norm_rows(rows)
    if not ordered:
        g, w = sorted(g, key=repr), sorted(w, key=repr)
    assert g == w, f"\n got: {g}\nwant: {w}"
