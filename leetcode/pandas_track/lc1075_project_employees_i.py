"""
1075. Project Employees I · Easy · https://leetcode.com/problems/project-employees-i/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    project = frame(['project_id', 'employee_id'], [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]], {'project_id': 'Int64', 'employee_id': 'Int64'})
    employee = frame(['employee_id', 'name', 'experience_years'], [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]], {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    check(project_employees_i(project, employee), ['project_id', 'average_years'], [[1, 2.0], [2, 2.5]], ordered=False)
