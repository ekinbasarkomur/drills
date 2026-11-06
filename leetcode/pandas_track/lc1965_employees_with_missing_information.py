"""
1965. Employees With Missing Information · Easy · https://leetcode.com/problems/employees-with-missing-information/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name'], [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']], {'employee_id': 'Int64', 'name': 'object'})
    salaries = frame(['employee_id', 'salary'], [[5, 76071], [1, 22517], [4, 63539]], {'employee_id': 'Int64', 'salary': 'Int64'})
    check(find_employees(employees, salaries), ['employee_id'], [[1], [2]], ordered=True)
