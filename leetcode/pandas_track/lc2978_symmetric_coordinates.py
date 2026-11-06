"""
2978. Symmetric Coordinates · Medium · https://leetcode.com/problems/symmetric-coordinates/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    coordinates = frame(['X', 'Y'], [[20, 20], [20, 20], [20, 21], [23, 22], [22, 23], [21, 20]], {'X': 'Int64', 'Y': 'Int64'})
    check(symmetric_pairs(coordinates), ['x', 'y'], [[20, 20], [20, 21], [22, 23]], ordered=True)
