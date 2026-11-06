"""
1939. Users That Actively Request Confirmation Messages · Easy · https://leetcode.com/problems/users-that-actively-request-confirmation-messages/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    signups = frame(['user_id', 'time_stamp'], [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'], [6, '2020-12-09 10:39:37']], {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    confirmations = frame(['user_id', 'time_stamp', 'action'], [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-01-06 03:37:45', 'timeout'], [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 11:57:30', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'], [2, '2021-01-23 00:00:00', 'timeout'], [6, '2021-10-23 14:14:14', 'confirmed'], [6, '2021-10-24 14:14:13', 'timeout']], {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})
    check(find_requesting_users(signups, confirmations), ['user_id'], [[2], [3], [6]], ordered=False)
