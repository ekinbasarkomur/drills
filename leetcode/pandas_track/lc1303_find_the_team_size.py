"""
1303. Find the Team Size · Easy · https://leetcode.com/problems/find-the-team-size/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['employee_id', 'team_id'], [[1, 8], [2, 8], [3, 8], [4, 7], [5, 9], [6, 9]], {'employee_id': 'Int64', 'team_id': 'Int64'})
    check(team_size(employee), ['employee_id', 'team_size'], [[1, 3], [2, 3], [3, 3], [4, 1], [5, 2], [6, 2]], ordered=False)
