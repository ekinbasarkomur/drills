"""
176. Second Highest Salary · Medium · https://leetcode.com/problems/second-highest-salary/
Plan: 30 Days of Pandas · Gün 11 · Data Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'salary'], [[1, 100], [2, 200], [3, 300]], {'id': 'int64', 'salary': 'int64'})
    check(second_highest_salary(employee), ['SecondHighestSalary'], [[200]], ordered=False)


def test_example_2():
    employee = frame(['id', 'salary'], [[1, 100]], {'id': 'int64', 'salary': 'int64'})
    check(second_highest_salary(employee), ['SecondHighestSalary'], [[None]], ordered=False)
