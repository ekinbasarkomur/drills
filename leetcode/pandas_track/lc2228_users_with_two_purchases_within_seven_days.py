"""
2228. Users With Two Purchases Within Seven Days · Medium · https://leetcode.com/problems/users-with-two-purchases-within-seven-days/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    purchases = frame(['purchase_id', 'user_id', 'purchase_date'], [[4, 2, '2022-03-13'], [1, 5, '2022-02-11'], [3, 7, '2022-06-19'], [6, 2, '2022-03-20'], [5, 7, '2022-06-19'], [2, 2, '2022-06-08']], {'purchase_id': 'Int64', 'user_id': 'Int64', 'purchase_date': 'datetime64[ns]'})
    check(find_valid_users(purchases), ['user_id'], [[2], [7]], ordered=True)
