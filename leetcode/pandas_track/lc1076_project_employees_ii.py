"""
1076. Project Employees II · Easy · https://leetcode.com/problems/project-employees-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    project = frame(['project_id', 'employee_id'], [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]], {'project_id': 'Int64', 'employee_id': 'Int64'})
    employee = frame(['employee_id', 'name', 'experience_years'], [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]], {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    check(project_employees_ii(project, employee), ['project_id'], [[1]], ordered=False)
