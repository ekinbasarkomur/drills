"""
1783. Grand Slam Titles · Medium · https://leetcode.com/problems/grand-slam-titles/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    players = frame(['player_id', 'player_name'], [[1, 'Nadal'], [2, 'Federer'], [3, 'Novak']], {'player_id': 'Int64', 'player_name': 'object'})
    championships = frame(['year', 'Wimbledon', 'Fr_open', 'US_open', 'Au_open'], [[2018, 1, 1, 1, 1], [2019, 1, 1, 2, 2], [2020, 2, 1, 2, 2]], {'year': 'Int64', 'Wimbledon': 'Int64', 'Fr_open': 'Int64', 'US_open': 'Int64', 'Au_open': 'Int64'})
    check(grand_slam_titles(players, championships), ['player_id', 'player_name', 'grand_slams_count'], [[2, 'Federer', 5], [1, 'Nadal', 7]], ordered=False)
