"""
2880. Select Data · Easy · https://leetcode.com/problems/select-data/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'name', 'age'], [[101, 'Ulysses', 13], [53, 'William', 10], [128, 'Henry', 6], [3, 'Henry', 11]], {'student_id': 'Int64', 'name': 'object', 'age': 'Int64'})
    check(selectData(students), ['name', 'age'], [['Ulysses', 13]], ordered=False)
