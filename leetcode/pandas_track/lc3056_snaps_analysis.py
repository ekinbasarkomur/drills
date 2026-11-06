"""
3056. Snaps Analysis · Medium · https://leetcode.com/problems/snaps-analysis/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    activities = frame(['activity_id', 'user_id', 'activity_type', 'time_spent'], [[7274, 123, 'open', 4.5], [2425, 123, 'send', 3.5], [1413, 456, 'send', 5.67], [2536, 456, 'open', 3.0], [8564, 456, 'send', 8.24], [5235, 789, 'send', 6.24], [4251, 123, 'open', 1.25], [1435, 789, 'open', 5.25]], {'activity_id': 'Int64', 'user_id': 'Int64', 'activity_type': 'object', 'time_spent': 'Float64'})
    age = frame(['user_id', 'age_bucket'], [[123, '31-35'], [789, '21-25'], [456, '26-30']], {'user_id': 'Int64', 'age_bucket': 'object'})
    check(snap_analysis(activities, age), ['age_bucket', 'send_perc', 'open_perc'], [['31-35', 37.84, 62.16], ['26-30', 82.26, 17.74], ['21-25', 54.31, 45.69]], ordered=False)
