"""
1890. The Latest Login in 2020 · Easy · https://leetcode.com/problems/the-latest-login-in-2020/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    logins = frame(['user_id', 'time_stamp'], [[6, '2020-06-30 15:06:07'], [6, '2021-04-21 14:06:06'], [6, '2019-03-07 00:18:15'], [8, '2020-02-01 05:10:53'], [8, '2020-12-30 00:46:50'], [2, '2020-01-16 02:49:50'], [2, '2019-08-25 07:59:08'], [14, '2019-07-14 09:00:00'], [14, '2021-01-06 11:59:59']], {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    check(latest_login(logins), ['user_id', 'last_stamp'], [[6, '2020-06-30 15:06:07'], [8, '2020-12-30 00:46:50'], [2, '2020-01-16 02:49:50']], ordered=False)
