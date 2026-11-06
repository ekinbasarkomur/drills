"""
1809. Ad-Free Sessions · Easy · https://leetcode.com/problems/ad-free-sessions/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    playback = frame(['session_id', 'customer_id', 'start_time', 'end_time'], [[1, 1, 1, 5], [2, 1, 15, 23], [3, 2, 10, 12], [4, 2, 17, 28], [5, 2, 2, 8]], {'session_id': 'Int64', 'customer_id': 'Int64', 'start_time': 'Int64', 'end_time': 'Int64'})
    ads = frame(['ad_id', 'customer_id', 'timestamp'], [[1, 1, 5], [2, 2, 17], [3, 2, 20]], {'ad_id': 'Int64', 'customer_id': 'Int64', 'timestamp': 'Int64'})
    check(ad_free_sessions(playback, ads), ['session_id'], [[2], [3], [5]], ordered=False)
