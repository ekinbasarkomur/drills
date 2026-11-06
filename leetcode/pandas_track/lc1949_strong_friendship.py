"""
1949. Strong Friendship · Medium · https://leetcode.com/problems/strong-friendship/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friendship = frame(['user1_id', 'user2_id'], [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [1, 5], [2, 5], [1, 7], [3, 7], [1, 6], [3, 6], [2, 6]], {'user1_id': 'Int64', 'user2_id': 'Int64'})
    check(strong_friendship(friendship), ['user1_id', 'user2_id', 'common_friend'], [[1, 2, 4], [1, 3, 3]], ordered=False)
