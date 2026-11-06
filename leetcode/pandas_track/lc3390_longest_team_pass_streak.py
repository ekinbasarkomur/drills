"""
3390. Longest Team Pass Streak · Hard · https://leetcode.com/problems/longest-team-pass-streak/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_longest_streaks(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    teams = frame(['player_id', 'team_name'], [[1, 'Arsenal'], [2, 'Arsenal'], [3, 'Arsenal'], [4, 'Arsenal'], [5, 'Chelsea'], [6, 'Chelsea'], [7, 'Chelsea'], [8, 'Chelsea']], {})
    passes = frame(['pass_from', 'time_stamp', 'pass_to'], [[1, '00:05', 2], [2, '00:07', 3], [3, '00:08', 4], [4, '00:10', 5], [6, '00:15', 7], [7, '00:17', 8], [8, '00:20', 6], [6, '00:22', 5], [1, '00:25', 2], [2, '00:27', 3]], {})
    check(calculate_longest_streaks(teams, passes), ['team_name', 'longest_streak'], [['Arsenal', 3], ['Chelsea', 4]], ordered=True)
