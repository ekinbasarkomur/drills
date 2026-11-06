"""
1892. Page Recommendations II · Hard · https://leetcode.com/problems/page-recommendations-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def recommend_page(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friendship = frame(['user1_id', 'user2_id'], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [6, 1]], {'user1_id': 'Int64', 'user2_id': 'Int64'})
    likes = frame(['user_id', 'page_id'], [[1, 88], [2, 23], [3, 24], [4, 56], [5, 11], [6, 33], [2, 77], [3, 77], [6, 88]], {'user_id': 'Int64', 'page_id': 'Int64'})
    check(recommend_page(friendship, likes), ['user_id', 'page_id', 'friends_likes'], [[1, 77, 2], [1, 23, 1], [1, 24, 1], [1, 56, 1], [1, 33, 1], [2, 24, 1], [2, 56, 1], [2, 11, 1], [2, 88, 1], [3, 88, 1], [3, 23, 1], [4, 88, 1], [4, 77, 1], [4, 23, 1], [5, 77, 1], [5, 23, 1]], ordered=False)
