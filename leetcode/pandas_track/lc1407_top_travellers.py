"""
1407. Top Travellers · Easy · https://leetcode.com/problems/top-travellers/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['id', 'name'], [[1, 'Alice'], [2, 'Bob'], [3, 'Alex'], [4, 'Donald'], [7, 'Lee'], [13, 'Jonathan'], [19, 'Elvis']], {'id': 'Int64', 'name': 'object'})
    rides = frame(['id', 'user_id', 'distance'], [[1, 1, 120], [2, 2, 317], [3, 3, 222], [4, 7, 100], [5, 13, 312], [6, 19, 50], [7, 7, 120], [8, 19, 400], [9, 7, 230]], {'id': 'Int64', 'user_id': 'Int64', 'distance': 'Int64'})
    check(top_travellers(users, rides), ['name', 'travelled_distance'], [['Elvis', 450], ['Lee', 450], ['Bob', 317], ['Jonathan', 312], ['Alex', 222], ['Alice', 120], ['Donald', 0]], ordered=True)
