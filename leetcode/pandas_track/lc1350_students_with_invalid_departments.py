"""
1350. Students With Invalid Departments · Easy · https://leetcode.com/problems/students-with-invalid-departments/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    departments = frame(['id', 'name'], [[1, 'Electrical Engineering'], [7, 'Computer Engineering'], [13, 'Bussiness Administration']], {'id': 'Int64', 'name': 'object'})
    students = frame(['id', 'name', 'department_id'], [[23, 'Alice', 1], [1, 'Bob', 7], [5, 'Jennifer', 13], [2, 'John', 14], [4, 'Jasmine', 77], [3, 'Steve', 74], [6, 'Luis', 1], [8, 'Jonathan', 7], [7, 'Daiana', 33], [11, 'Madelynn', 1]], {'id': 'Int64', 'name': 'object', 'department_id': 'Int64'})
    check(find_students(departments, students), ['id', 'name'], [[2, 'John'], [7, 'Daiana'], [4, 'Jasmine'], [3, 'Steve']], ordered=False)
