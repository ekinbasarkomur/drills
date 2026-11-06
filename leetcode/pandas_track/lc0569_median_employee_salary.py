"""
569. Median Employee Salary · Hard · https://leetcode.com/problems/median-employee-salary/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'company', 'salary'], [[1, 'A', 2341], [2, 'A', 341], [3, 'A', 15], [4, 'A', 15314], [5, 'A', 451], [6, 'A', 513], [7, 'B', 15], [8, 'B', 13], [9, 'B', 1154], [10, 'B', 1345], [11, 'B', 1221], [12, 'B', 234], [13, 'C', 2345], [14, 'C', 2645], [15, 'C', 2645], [16, 'C', 2652], [17, 'C', 65]], {'id': 'Int64', 'company': 'object', 'salary': 'Int64'})
    check(median_employee_salary(employee), ['id', 'company', 'salary'], [[5, 'A', 451], [6, 'A', 513], [12, 'B', 234], [9, 'B', 1154], [14, 'C', 2645]], ordered=False)
