"""
1841. League Statistics · Medium · https://leetcode.com/problems/league-statistics/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    teams = frame(['team_id', 'team_name'], [[1, 'Ajax'], [4, 'Dortmund'], [6, 'Arsenal']], {'team_id': 'Int64', 'team_name': 'object'})
    matches = frame(['home_team_id', 'away_team_id', 'home_team_goals', 'away_team_goals'], [[1, 4, 0, 1], [1, 6, 3, 3], [4, 1, 5, 2], [6, 1, 0, 0]], {'home_team_id': 'Int64', 'away_team_id': 'Int64', 'home_team_goals': 'Int64', 'away_team_goals': 'Int64'})
    check(league_statistics(teams, matches), ['team_name', 'matches_played', 'points', 'goal_for', 'goal_against', 'goal_diff'], [['Dortmund', 2, 6, 6, 2, 4], ['Arsenal', 2, 2, 3, 3, 0], ['Ajax', 4, 2, 5, 9, -4]], ordered=True)
