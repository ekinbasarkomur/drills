"""
2688. Find Active Users · Medium · https://leetcode.com/problems/find-active-users/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_active_users(users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'item', 'created_at', 'amount'], [[5, 'Smart Crock Pot', '2021-09-18', 698882], [6, 'Smart Lock', '2021-09-14', 11487], [6, 'Smart Thermostat', '2021-09-10', 674762], [8, 'Smart Light Strip', '2021-09-29', 630773], [4, 'Smart Cat Feeder', '2021-09-02', 693545], [4, 'Smart Bed', '2021-09-13', 170249]], {'user_id': 'Int64', 'item': 'object', 'created_at': 'datetime64[ns]', 'amount': 'Int64'})
    check(find_active_users(users), ['user_id'], [[6]], ordered=False)
