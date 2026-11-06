"""
613. Shortest Distance in a Line · Easy · https://leetcode.com/problems/shortest-distance-in-a-line/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    point = frame(['x'], [[-1], [0], [2]], {'x': 'Int64'})
    check(shortest_distance(point), ['shortest'], [[1]], ordered=False)
