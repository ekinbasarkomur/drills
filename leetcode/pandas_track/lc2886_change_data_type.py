"""
2886. Change Data Type · Easy · https://leetcode.com/problems/change-data-type/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'name', 'age', 'grade'], [[1, 'Ava', 6, 73.0], [2, 'Kate', 15, 87.0]], {'student_id': 'Int64', 'name': 'object', 'age': 'Int64', 'grade': 'Float64'})
    check(changeDatatype(students), ['student_id', 'name', 'age', 'grade'], [[1, 'Ava', 6, 73], [2, 'Kate', 15, 87]], ordered=False)
