"""
3089. Find Bursty Behavior · Medium · https://leetcode.com/problems/find-bursty-behavior/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_bursty_behavior(posts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    posts = frame(['post_id', 'user_id', 'post_date'], [[1, 1, '2024-02-27'], [2, 5, '2024-02-06'], [3, 3, '2024-02-25'], [4, 3, '2024-02-14'], [5, 3, '2024-02-06'], [6, 2, '2024-02-25']], {'post_id': 'Int64', 'user_id': 'Int64', 'post_date': 'datetime64[ns]'})
    check(find_bursty_behavior(posts), ['user_id', 'max_7day_posts', 'avg_weekly_posts'], [[1, 1, 0.25], [2, 1, 0.25], [5, 1, 0.25]], ordered=True)
