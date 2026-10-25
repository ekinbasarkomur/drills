"""
2889. Reshape Data: Pivot · Easy · https://leetcode.com/problems/reshape-data-pivot/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: turn the long table into a wide one: one row per month, one column per city, temperatures as values.
Approach: pivot(index="month", columns="city", values="temperature"); index and columns come out sorted
Time O(n log n), space O(n)
"""

from typing import List

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")


# ---------------------------------------------------------------- tests


def test_example_1():
    weather = frame(
        ["city", "month", "temperature"],
        [
            ["Jacksonville", "January", 13],
            ["Jacksonville", "February", 23],
            ["Jacksonville", "March", 38],
            ["Jacksonville", "April", 5],
            ["Jacksonville", "May", 34],
            ["ElPaso", "January", 20],
            ["ElPaso", "February", 6],
            ["ElPaso", "March", 26],
            ["ElPaso", "April", 2],
            ["ElPaso", "May", 43],
        ],
    )
    got = pivotTable(weather)
    # LeetCode: satırlar ay (alfabetik), sütunlar şehir (alfabetik)
    assert list(got.index) == ["April", "February", "January", "March", "May"]
    assert list(got.columns) == ["ElPaso", "Jacksonville"]
    assert got.values.tolist() == [[2, 5], [6, 23], [20, 13], [26, 38], [43, 34]]
