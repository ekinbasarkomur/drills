"""
1264. Page Recommendations · Medium · https://leetcode.com/problems/page-recommendations/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friendship = frame(['user1_id', 'user2_id'], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [6, 1]], {'user1_id': 'Int64', 'user2_id': 'Int64'})
    likes = frame(['user_id', 'page_id'], [[1, 88], [2, 23], [3, 24], [4, 56], [5, 11], [6, 33], [2, 77], [3, 77], [6, 88]], {'user_id': 'Int64', 'page_id': 'Int64'})
    check(page_recommendations(friendship, likes), ['recommended_page'], [[23], [24], [56], [33], [77]], ordered=False)
