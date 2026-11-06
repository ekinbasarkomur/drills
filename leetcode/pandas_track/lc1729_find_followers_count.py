"""
1729. Find Followers Count · Easy · https://leetcode.com/problems/find-followers-count/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    followers = frame(['user_id', 'follower_id'], [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']], {'user_id': 'Int64', 'follower_id': 'Int64'})
    check(count_followers(followers), ['user_id', 'followers_count'], [[0, 1], [1, 1], [2, 2]], ordered=True)
