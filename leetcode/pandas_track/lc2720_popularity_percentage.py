"""
2720. Popularity Percentage · Hard · https://leetcode.com/problems/popularity-percentage/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friends = frame(['user1', 'user2'], [[2, 1], [1, 3], [4, 1], [1, 5], [1, 6], [2, 6], [7, 2], [8, 3], [3, 9]], {'user1': 'Int64', 'user2': 'Int64'})
    check(popularity_percentage(friends), ['user1', 'percentage_popularity'], [[1, 55.56], [2, 33.33], [3, 33.33], [4, 11.11], [5, 11.11], [6, 22.22], [7, 11.11], [8, 11.11], [9, 11.11]], ordered=True)
