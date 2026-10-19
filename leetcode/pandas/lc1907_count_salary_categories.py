"""
1907. Count Salary Categories · Medium · https://leetcode.com/problems/count-salary-categories/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    accounts = frame(['account_id', 'income'], [[3, 108939], [2, 12747], [8, 87709], [6, 91796]], {'account_id': 'Int64', 'income': 'Int64'})
    check(count_salary_categories(accounts), ['category', 'accounts_count'], [['Low Salary', 1], ['Average Salary', 0], ['High Salary', 3]], ordered=False)
