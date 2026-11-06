"""
3252. Premier League Table Ranking II · Medium · https://leetcode.com/problems/premier-league-table-ranking-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    team_stats = frame(['team_id', 'team_name', 'matches_played', 'wins', 'draws', 'losses'], [[1, 'Chelsea', 22, 13, 2, 7], [2, 'Nottingham Forest', 27, 6, 6, 15], [3, 'Liverpool', 17, 1, 8, 8], [4, 'Aston Villa', 20, 1, 6, 13], [5, 'Fulham', 31, 18, 1, 12], [6, 'Burnley', 26, 6, 9, 11], [7, 'Newcastle United', 33, 11, 10, 12], [8, 'Sheffield United', 20, 18, 2, 0], [9, 'Luton Town', 5, 4, 0, 1], [10, 'Everton', 14, 2, 6, 6]], {})
    check(calculate_team_tiers(team_stats), ['team_name', 'points', 'position', 'tier'], [['Sheffield United', 56, 1, 'Tier 1'], ['Fulham', 55, 2, 'Tier 1'], ['Newcastle United', 43, 3, 'Tier 1'], ['Chelsea', 41, 4, 'Tier 1'], ['Burnley', 27, 5, 'Tier 2'], ['Nottingham Forest', 24, 6, 'Tier 2'], ['Everton', 12, 7, 'Tier 2'], ['Luton Town', 12, 7, 'Tier 2'], ['Liverpool', 11, 9, 'Tier 3'], ['Aston Villa', 9, 10, 'Tier 3']], ordered=True)
