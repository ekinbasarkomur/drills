"""
511. Game Play Analysis I · Easy · https://leetcode.com/problems/game-play-analysis-i/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    activity = frame(['player_id', 'device_id', 'event_date', 'games_played'], [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]], {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    check(game_analysis(activity), ['player_id', 'first_login'], [[1, '2016-03-01'], [2, '2017-06-25'], [3, '2016-03-02']], ordered=False)
