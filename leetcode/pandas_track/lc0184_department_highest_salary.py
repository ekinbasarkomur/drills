"""
184. Department Highest Salary · Medium · https://leetcode.com/problems/department-highest-salary/
Plan: 30 Days of Pandas · Gün 12 · Data Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'name', 'salary', 'departmentId'], [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]], {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    department = frame(['id', 'name'], [[1, 'IT'], [2, 'Sales']], {'id': 'Int64', 'name': 'object'})
    check(department_highest_salary(employee, department), ['Department', 'Employee', 'Salary'], [['IT', 'Jim', 90000], ['Sales', 'Henry', 80000], ['IT', 'Max', 90000]], ordered=False)
