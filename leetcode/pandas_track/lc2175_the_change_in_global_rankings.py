"""
2175. The Change in Global Rankings · Medium · https://leetcode.com/problems/the-change-in-global-rankings/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    team_points = frame(['team_id', 'name', 'points'], [[3, 'Algeria', 1431], [1, 'Senegal', 2132], [2, 'New Zealand', 1402], [4, 'Croatia', 1817]], {'team_id': 'Int64', 'name': 'object', 'points': 'Int64'})
    points_change = frame(['team_id', 'points_change'], [[3, 399], [2, 0], [4, 13], [1, -22]], {'team_id': 'Int64', 'points_change': 'Int64'})
    check(global_ratings_change(team_points, points_change), ['team_id', 'name', 'rank_diff'], [[1, 'Senegal', 0], [4, 'Croatia', -1], [3, 'Algeria', 1], [2, 'New Zealand', 0]], ordered=False)
