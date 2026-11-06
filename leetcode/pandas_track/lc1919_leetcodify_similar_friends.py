"""
1919. Leetcodify Similar Friends · Hard · https://leetcode.com/problems/leetcodify-similar-friends/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def leetcodify_similar_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    listens = frame(['user_id', 'song_id', 'day'], [[1, 10, '2021-03-15'], [1, 11, '2021-03-15'], [1, 12, '2021-03-15'], [2, 10, '2021-03-15'], [2, 11, '2021-03-15'], [2, 12, '2021-03-15'], [3, 10, '2021-03-15'], [3, 11, '2021-03-15'], [3, 12, '2021-03-15'], [4, 10, '2021-03-15'], [4, 11, '2021-03-15'], [4, 13, '2021-03-15'], [5, 10, '2021-03-16'], [5, 11, '2021-03-16'], [5, 12, '2021-03-16']], {'user_id': 'Int64', 'song_id': 'Int64', 'day': 'datetime64[ns]'})
    friendship = frame(['user1_id', 'user2_id'], [[1, 2], [2, 4], [2, 5]], {'user1_id': 'Int64', 'user2_id': 'Int64'})
    check(leetcodify_similar_friends(listens, friendship), ['user1_id', 'user2_id'], [[1, 2]], ordered=False)
