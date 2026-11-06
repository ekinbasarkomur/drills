"""
1633. Percentage of Users Attended a Contest · Easy · https://leetcode.com/problems/percentage-of-users-attended-a-contest/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'user_name'], [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']], {'user_id': 'Int64', 'user_name': 'object'})
    register = frame(['contest_id', 'user_id'], [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]], {'contest_id': 'Int64', 'user_id': 'Int64'})
    check(users_percentage(users, register), ['contest_id', 'percentage'], [[208, 100.0], [209, 100.0], [210, 100.0], [215, 66.67], [207, 33.33]], ordered=True)
