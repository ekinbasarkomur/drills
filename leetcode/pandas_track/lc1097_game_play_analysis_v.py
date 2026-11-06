"""
1097. Game Play Analysis V · Hard · https://leetcode.com/problems/game-play-analysis-v/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    activity = frame(['player_id', 'device_id', 'event_date', 'games_played'], [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-01', 0], [3, 4, '2018-07-03', 5]], {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    check(gameplay_analysis(activity), ['install_dt', 'installs', 'Day1_retention'], [['2016-03-01', 2, 0.5], ['2017-06-25', 1, 0.0]], ordered=False)
