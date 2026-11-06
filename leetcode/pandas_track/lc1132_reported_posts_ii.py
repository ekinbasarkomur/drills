"""
1132. Reported Posts II · Medium · https://leetcode.com/problems/reported-posts-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    actions = frame(['user_id', 'post_id', 'action_date', 'action', 'extra'], [[1, 1, '2019-07-01', 'view', None], [1, 1, '2019-07-01', 'like', None], [1, 1, '2019-07-01', 'share', None], [2, 2, '2019-07-04', 'view', None], [2, 2, '2019-07-04', 'report', 'spam'], [3, 4, '2019-07-04', 'view', None], [3, 4, '2019-07-04', 'report', 'spam'], [4, 3, '2019-07-02', 'view', None], [4, 3, '2019-07-02', 'report', 'spam'], [5, 2, '2019-07-03', 'view', None], [5, 2, '2019-07-03', 'report', 'racism'], [5, 5, '2019-07-03', 'view', None], [5, 5, '2019-07-03', 'report', 'racism']], {'user_id': 'Int64', 'post_id': 'Int64', 'action_date': 'datetime64[ns]', 'action': 'object', 'extra': 'object'})
    removals = frame(['post_id', 'remove_date'], [[2, '2019-07-20'], [3, '2019-07-18']], {'post_id': 'Int64', 'remove_date': 'datetime64[ns]'})
    check(reported_posts(actions, removals), ['average_daily_percent'], [[75.0]], ordered=False)
