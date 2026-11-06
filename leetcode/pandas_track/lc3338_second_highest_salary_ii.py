"""
3338. Second Highest Salary II · Medium · https://leetcode.com/problems/second-highest-salary-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['emp_id', 'salary', 'dept'], [[1, 70000, 'Sales'], [2, 80000, 'Sales'], [3, 80000, 'Sales'], [4, 90000, 'Sales'], [5, 55000, 'IT'], [6, 65000, 'IT'], [7, 65000, 'IT'], [8, 50000, 'Marketing'], [9, 55000, 'Marketing'], [10, 55000, 'HR']], {})
    check(find_second_highest_salary(employees), ['emp_id', 'dept'], [[2, 'Sales'], [3, 'Sales'], [5, 'IT'], [8, 'Marketing']], ordered=True)
