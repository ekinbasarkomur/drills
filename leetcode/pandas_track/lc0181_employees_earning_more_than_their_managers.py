"""
181. Employees Earning More Than Their Managers · Easy · https://leetcode.com/problems/employees-earning-more-than-their-managers/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'name', 'salary', 'managerId'], [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]], {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})
    check(find_employees(employee), ['Employee'], [['Joe']], ordered=False)
