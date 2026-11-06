"""
1142. User Activity for the Past 30 Days II · Easy · https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    activity = frame(['user_id', 'session_id', 'activity_date', 'activity_type'], [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [3, 5, '2019-07-21', 'open_session'], [3, 5, '2019-07-21', 'scroll_down'], [3, 5, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']], {'user_id': 'Int64', 'session_id': 'Int64', 'activity_date': 'datetime64[ns]', 'activity_type': 'object'})
    check(user_activity(activity), ['average_sessions_per_user'], [[1.33]], ordered=False)
