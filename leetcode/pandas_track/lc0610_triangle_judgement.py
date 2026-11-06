"""
610. Triangle Judgement · Easy · https://leetcode.com/problems/triangle-judgement/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    triangle = frame(['x', 'y', 'z'], [[13, 15, 30], [10, 20, 15]], {'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
    check(triangle_judgement(triangle), ['x', 'y', 'z', 'triangle'], [[13, 15, 30, 'No'], [10, 20, 15, 'Yes']], ordered=False)
