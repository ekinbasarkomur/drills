"""
2885. Rename Columns · Easy · https://leetcode.com/problems/rename-columns/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['id', 'first', 'last', 'age'], [[1, 'Mason', 'King', 6], [2, 'Ava', 'Wright', 7], [3, 'Taylor', 'Hall', 16], [4, 'Georgia', 'Thompson', 18], [5, 'Thomas', 'Moore', 10]], {'id': 'Int64', 'first': 'object', 'last': 'object', 'age': 'Int64'})
    check(renameColumns(students), ['student_id', 'first_name', 'last_name', 'age_in_years'], [[1, 'Mason', 'King', 6], [2, 'Ava', 'Wright', 7], [3, 'Taylor', 'Hall', 16], [4, 'Georgia', 'Thompson', 18], [5, 'Thomas', 'Moore', 10]], ordered=False)
