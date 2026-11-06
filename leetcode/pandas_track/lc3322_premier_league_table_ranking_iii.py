"""
3322. Premier League Table Ranking III · Medium · https://leetcode.com/problems/premier-league-table-ranking-iii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def process_team_standings(season_stats: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    season_stats = frame(['season_id', 'team_id', 'team_name', 'matches_played', 'wins', 'draws', 'losses', 'goals_for', 'goals_against'], [[2021, 1, 'Manchester City', 38, 29, 6, 3, 99, 26], [2021, 2, 'Liverpool', 38, 28, 8, 2, 94, 26], [2021, 3, 'Chelsea', 38, 21, 11, 6, 76, 33], [2021, 4, 'Tottenham', 38, 22, 5, 11, 69, 40], [2021, 5, 'Arsenal', 38, 22, 3, 13, 61, 48], [2022, 1, 'Manchester City', 38, 28, 5, 5, 94, 33], [2022, 2, 'Arsenal', 38, 26, 6, 6, 88, 43], [2022, 3, 'Manchester United', 38, 23, 6, 9, 58, 43], [2022, 4, 'Newcastle', 38, 19, 14, 5, 68, 33], [2022, 5, 'Liverpool', 38, 19, 10, 9, 75, 47]], {})
    check(process_team_standings(season_stats), ['season_id', 'team_id', 'team_name', 'points', 'goal_difference', 'position'], [[2021, 1, 'Manchester City', 93, 73, 1], [2021, 2, 'Liverpool', 92, 68, 2], [2021, 3, 'Chelsea', 74, 43, 3], [2021, 4, 'Tottenham', 71, 29, 4], [2021, 5, 'Arsenal', 69, 13, 5], [2022, 1, 'Manchester City', 89, 61, 1], [2022, 2, 'Arsenal', 84, 45, 2], [2022, 3, 'Manchester United', 75, 15, 3], [2022, 4, 'Newcastle', 71, 35, 4], [2022, 5, 'Liverpool', 67, 28, 5]], ordered=True)
