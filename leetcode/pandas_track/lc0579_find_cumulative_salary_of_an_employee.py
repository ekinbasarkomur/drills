"""
579. Find Cumulative Salary of an Employee · Hard · https://leetcode.com/problems/find-cumulative-salary-of-an-employee/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'month', 'salary'], [[1, 1, 20], [2, 1, 20], [1, 2, 30], [2, 2, 30], [3, 2, 40], [1, 3, 40], [3, 3, 60], [1, 4, 60], [3, 4, 70], [1, 7, 90], [1, 8, 90]], {'id': 'Int64', 'month': 'Int64', 'salary': 'Int64'})
    check(cumulative_salary(employee), ['id', 'month', 'Salary'], [[1, 7, 90], [1, 4, 130], [1, 3, 90], [1, 2, 50], [1, 1, 20], [2, 1, 20], [3, 3, 100], [3, 2, 40]], ordered=True)
