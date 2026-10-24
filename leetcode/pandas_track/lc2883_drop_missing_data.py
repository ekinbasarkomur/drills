"""
2883. Drop Missing Data · Easy · https://leetcode.com/problems/drop-missing-data/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'name', 'age'], [[32, 'Piper', 5], [217, None, 19], [779, 'Georgia', 20], [849, 'Willow', 14]], {'student_id': 'Int64', 'name': 'object', 'age': 'Int64'})
    check(dropMissingData(students), ['student_id', 'name', 'age'], [[32, 'Piper', 5], [779, 'Georgia', 20], [849, 'Willow', 14]], ordered=False)
