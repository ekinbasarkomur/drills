"""
185. Department Top Three Salaries · Hard · https://leetcode.com/problems/department-top-three-salaries/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'name', 'salary', 'departmentId'], [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]], {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    department = frame(['id', 'name'], [[1, 'IT'], [2, 'Sales']], {'id': 'Int64', 'name': 'object'})
    check(top_three_salaries(employee, department), ['Department', 'Employee', 'Salary'], [['IT', 'Max', 90000], ['IT', 'Joe', 85000], ['IT', 'Randy', 85000], ['IT', 'Will', 70000], ['Sales', 'Henry', 80000], ['Sales', 'Sam', 60000]], ordered=False)
