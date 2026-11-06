"""
1972. First and Last Call On the Same Day · Hard · https://leetcode.com/problems/first-and-last-call-on-the-same-day/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    calls = frame(['caller_id', 'recipient_id', 'call_time'], [[8, 4, '2021-08-24 17:46:07'], [4, 8, '2021-08-24 19:57:13'], [5, 1, '2021-08-11 05:28:44'], [8, 3, '2021-08-17 04:04:15'], [11, 3, '2021-08-17 13:07:00'], [8, 11, '2021-08-17 22:22:22']], {'caller_id': 'Int64', 'recipient_id': 'Int64', 'call_time': 'datetime64[ns]'})
    check(same_day_calls(calls), ['user_id'], [[1], [4], [5], [8]], ordered=False)
