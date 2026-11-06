"""
3061. Calculate Trapping Rain Water · Hard · https://leetcode.com/problems/calculate-trapping-rain-water/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    heights = frame(['id', 'height'], [[1, 0], [2, 1], [3, 0], [4, 2], [5, 1], [6, 0], [7, 1], [8, 3], [9, 2], [10, 1], [11, 2], [12, 1]], {'id': 'Int64', 'height': 'Int64'})
    check(calculate_trapped_rain_water(heights), ['total_trapped_water'], [[6]], ordered=False)
