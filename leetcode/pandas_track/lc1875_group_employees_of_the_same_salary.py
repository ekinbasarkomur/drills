"""
1875. Group Employees of the Same Salary · Medium · https://leetcode.com/problems/group-employees-of-the-same-salary/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name', 'salary'], [[2, 'Meir', 3000], [3, 'Michael', 3000], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7400]], {'employee_id': 'Int64', 'name': 'object', 'salary': 'Int64'})
    check(employees_of_same_salary(employees), ['employee_id', 'name', 'salary', 'team_id'], [[2, 'Meir', 3000, 1], [3, 'Michael', 3000, 1], [7, 'Addilyn', 7400, 2], [9, 'Kannon', 7400, 2]], ordered=True)
