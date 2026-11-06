"""
1113. Reported Posts · Easy · https://leetcode.com/problems/reported-posts/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    actions = frame(['user_id', 'post_id', 'action_date', 'action', 'extra'], [[1, 1, '2019-07-01', 'view', None], [1, 1, '2019-07-01', 'like', None], [1, 1, '2019-07-01', 'share', None], [2, 4, '2019-07-04', 'view', None], [2, 4, '2019-07-04', 'report', 'spam'], [3, 4, '2019-07-04', 'view', None], [3, 4, '2019-07-04', 'report', 'spam'], [4, 3, '2019-07-02', 'view', None], [4, 3, '2019-07-02', 'report', 'spam'], [5, 2, '2019-07-04', 'view', None], [5, 2, '2019-07-04', 'report', 'racism'], [5, 5, '2019-07-04', 'view', None], [5, 5, '2019-07-04', 'report', 'racism']], {'user_id': 'Int64', 'post_id': 'Int64', 'action_date': 'datetime64[ns]', 'action': 'object', 'extra': 'object'})
    check(reported_posts(actions), ['report_reason', 'report_count'], [['spam', 1], ['racism', 2]], ordered=False)
