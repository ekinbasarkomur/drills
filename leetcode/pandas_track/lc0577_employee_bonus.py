"""
577. Employee Bonus · Easy · https://leetcode.com/problems/employee-bonus/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['empId', 'name', 'supervisor', 'salary'], [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]], {'empId': 'Int64', 'name': 'object', 'supervisor': 'Int64', 'salary': 'Int64'})
    bonus = frame(['empId', 'bonus'], [[2, 500], [4, 2000]], {'empId': 'Int64', 'bonus': 'Int64'})
    check(employee_bonus(employee, bonus), ['name', 'bonus'], [['Brad', None], ['John', None], ['Dan', 500]], ordered=False)
