"""
1454. Active Users · Medium · https://leetcode.com/problems/active-users/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    accounts = frame(['id', 'name'], [[1, 'Winston'], [7, 'Jonathan']], {'id': 'Int64', 'name': 'object'})
    logins = frame(['id', 'login_date'], [[7, '2020-05-30'], [1, '2020-05-30'], [7, '2020-05-31'], [7, '2020-06-01'], [7, '2020-06-02'], [7, '2020-06-02'], [7, '2020-06-03'], [1, '2020-06-07'], [7, '2020-06-10']], {'id': 'Int64', 'login_date': 'datetime64[ns]'})
    check(active_users(accounts, logins), ['id', 'name'], [[7, 'Jonathan']], ordered=True)
