"""
612. Shortest Distance in a Plane · Medium · https://leetcode.com/problems/shortest-distance-in-a-plane/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    point2_d = frame(['x', 'y'], [[-1, -1], [0, 0], [-1, -2]], {'x': 'Int64', 'y': 'Int64'})
    check(shortest_distance(point2_d), ['shortest'], [[1.0]], ordered=False)
