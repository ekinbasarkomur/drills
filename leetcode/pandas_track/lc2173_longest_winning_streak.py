"""
2173. Longest Winning Streak · Hard · https://leetcode.com/problems/longest-winning-streak/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    matches = frame(['player_id', 'match_day', 'result'], [[1, '2022-01-17', 'Win'], [1, '2022-01-18', 'Win'], [1, '2022-01-25', 'Win'], [1, '2022-01-31', 'Draw'], [1, '2022-02-08', 'Win'], [2, '2022-02-06', 'Lose'], [2, '2022-02-08', 'Lose'], [3, '2022-03-30', 'Win']], {'player_id': 'Int64', 'match_day': 'datetime64[ns]', 'result': 'object'})
    check(longest_winning_streak(matches), ['player_id', 'longest_streak'], [[1, 3], [2, 0], [3, 1]], ordered=False)
