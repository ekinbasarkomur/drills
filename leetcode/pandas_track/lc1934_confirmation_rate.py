"""
1934. Confirmation Rate · Medium · https://leetcode.com/problems/confirmation-rate/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    signups = frame(['user_id', 'time_stamp'], [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'], [6, '2020-12-09 10:39:37']], {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    confirmations = frame(['user_id', 'time_stamp', 'action'], [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'], [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'], [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'], [2, '2021-02-28 23:59:59', 'timeout']], {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})
    check(confirmation_rate(signups, confirmations), ['user_id', 'confirmation_rate'], [[6, 0.0], [3, 0.0], [7, 1.0], [2, 0.5]], ordered=False)
