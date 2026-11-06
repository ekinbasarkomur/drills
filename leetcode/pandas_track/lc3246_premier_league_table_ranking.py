"""
3246. Premier League Table Ranking · Easy · https://leetcode.com/problems/premier-league-table-ranking/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    team_stats = frame(['team_id', 'team_name', 'matches_played', 'wins', 'draws', 'losses'], [[1, 'Manchester City', 10, 6, 2, 2], [2, 'Liverpool', 10, 6, 2, 2], [3, 'Chelsea', 10, 5, 3, 2], [4, 'Arsenal', 10, 4, 4, 2], [5, 'Tottenham', 10, 3, 5, 2]], {})
    check(calculate_team_standings(team_stats), ['team_id', 'team_name', 'points', 'position'], [[2, 'Liverpool', 20, 1], [1, 'Manchester City', 20, 1], [3, 'Chelsea', 18, 3], [4, 'Arsenal', 16, 4], [5, 'Tottenham', 14, 5]], ordered=True)
