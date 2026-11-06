"""
1369. Get the Second Most Recent Activity · Hard · https://leetcode.com/problems/get-the-second-most-recent-activity/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_activity = frame(['username', 'activity', 'startDate', 'endDate'], [['Alice', 'Travel', '2020-02-12', '2020-02-20'], ['Alice', 'Dancing', '2020-02-21', '2020-02-23'], ['Alice', 'Travel', '2020-02-24', '2020-02-28'], ['Bob', 'Travel', '2020-02-11', '2020-02-18']], {'username': 'object', 'activity': 'object', 'startDate': 'datetime64[ns]', 'endDate': 'datetime64[ns]'})
    check(second_most_recent(user_activity), ['username', 'activity', 'startDate', 'endDate'], [['Alice', 'Dancing', '2020-02-21', '2020-02-23'], ['Bob', 'Travel', '2020-02-11', '2020-02-18']], ordered=False)
