"""
2339. All the Matches of the League · Easy · https://leetcode.com/problems/all-the-matches-of-the-league/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    teams = frame(['team_name'], [['Leetcode FC'], ['Ahly SC'], ['Real Madrid']], {'team_name': 'object'})
    check(find_all_matches(teams), ['home_team', 'away_team'], [['Real Madrid', 'Leetcode FC'], ['Real Madrid', 'Ahly SC'], ['Leetcode FC', 'Real Madrid'], ['Leetcode FC', 'Ahly SC'], ['Ahly SC', 'Real Madrid'], ['Ahly SC', 'Leetcode FC']], ordered=False)
