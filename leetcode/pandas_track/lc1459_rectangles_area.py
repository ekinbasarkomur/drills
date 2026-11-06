"""
1459. Rectangles Area · Medium · https://leetcode.com/problems/rectangles-area/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    points = frame(['id', 'x_value', 'y_value'], [[1, 2, 7], [2, 4, 8], [3, 2, 10]], {'id': 'Int64', 'x_value': 'Int64', 'y_value': 'Int64'})
    check(rectangles_area(points), ['p1', 'p2', 'area'], [[2, 3, 4], [1, 2, 2]], ordered=True)
