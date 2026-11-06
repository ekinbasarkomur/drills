"""
3384. Team Dominance by Pass Success · Hard · https://leetcode.com/problems/team-dominance-by-pass-success/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    teams = frame(['player_id', 'team_name'], [[1, 'Arsenal'], [2, 'Arsenal'], [3, 'Arsenal'], [4, 'Chelsea'], [5, 'Chelsea'], [6, 'Chelsea']], {})
    passes = frame(['pass_from', 'time_stamp', 'pass_to'], [[1, '00:15', 2], [2, '00:45', 3], [3, '01:15', 1], [4, '00:30', 1], [2, '46:00', 3], [3, '46:15', 4], [1, '46:45', 2], [5, '46:30', 6]], {})
    check(calculate_team_dominance(teams, passes), ['team_name', 'half_number', 'dominance'], [['Arsenal', 1, 3], ['Arsenal', 2, 1], ['Chelsea', 1, -1], ['Chelsea', 2, 1]], ordered=True)
