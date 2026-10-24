"""
2880. Select Data · Easy · https://leetcode.com/problems/select-data/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: the name and age of the student whose student_id is 101.
Approach: .loc[row mask, column list]: the mask picks rows where student_id == 101,
          the list keeps only name and age.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'name', 'age'], [[101, 'Ulysses', 13], [53, 'William', 10], [128, 'Henry', 6], [3, 'Henry', 11]], {'student_id': 'Int64', 'name': 'object', 'age': 'Int64'})
    check(selectData(students), ['name', 'age'], [['Ulysses', 13]], ordered=False)
