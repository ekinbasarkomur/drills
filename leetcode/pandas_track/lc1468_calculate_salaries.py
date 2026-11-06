"""
1468. Calculate Salaries · Medium · https://leetcode.com/problems/calculate-salaries/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    salaries = frame(['company_id', 'employee_id', 'employee_name', 'salary'], [[1, 1, 'Tony', 2000], [1, 2, 'Pronub', 21300], [1, 3, 'Tyrrox', 10800], [2, 1, 'Pam', 300], [2, 7, 'Bassem', 450], [2, 9, 'Hermione', 700], [3, 7, 'Bocaben', 100], [3, 2, 'Ognjen', 2200], [3, 13, 'Nyancat', 3300], [3, 15, 'Morninngcat', 7777]], {'company_id': 'Int64', 'employee_id': 'Int64', 'employee_name': 'object', 'salary': 'Int64'})
    check(calculate_salaries(salaries), ['company_id', 'employee_id', 'employee_name', 'salary'], [[1, 1, 'Tony', 1020], [1, 2, 'Pronub', 10863], [1, 3, 'Tyrrox', 5508], [2, 1, 'Pam', 300], [2, 7, 'Bassem', 450], [2, 9, 'Hermione', 700], [3, 7, 'Bocaben', 76], [3, 2, 'Ognjen', 1672], [3, 13, 'Nyancat', 2508], [3, 15, 'Morninngcat', 5911]], ordered=False)
