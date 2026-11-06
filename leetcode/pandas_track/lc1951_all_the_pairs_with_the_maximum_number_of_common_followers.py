"""
1951. All the Pairs With the Maximum Number of Common Followers · Medium · https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    relations = frame(['user_id', 'follower_id'], [[1, 3], [2, 3], [7, 3], [1, 4], [2, 4], [7, 4], [1, 5], [2, 6], [7, 5]], {'user_id': 'Int64', 'follower_id': 'Int64'})
    check(find_pairs(relations), ['user1_id', 'user2_id'], [[1, 7]], ordered=False)
