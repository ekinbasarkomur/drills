"""
3118. Friday Purchase III  · Medium · https://leetcode.com/problems/friday-purchase-iii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def friday_purchases(purchases: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    purchases = frame(['user_id', 'purchase_date', 'amount_spend'], [[11, '2023-11-03', 1126], [15, '2023-11-10', 7473], [17, '2023-11-17', 2414], [12, '2023-11-24', 9692], [8, '2023-11-24', 5117], [1, '2023-11-24', 5241], [10, '2023-11-22', 8266], [13, '2023-11-21', 12000]], {'user_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'amount_spend': 'Int64'})
    users = frame(['user_id', 'membership'], [[11, 'Premium'], [15, 'VIP'], [17, 'Standard'], [12, 'VIP'], [8, 'Premium'], [1, 'VIP'], [10, 'Standard'], [13, 'Premium']], {})
    check(friday_purchases(purchases, users), ['week_of_month', 'membership', 'total_amount'], [[1, 'Premium', 1126], [1, 'VIP', 0], [2, 'Premium', 0], [2, 'VIP', 7473], [3, 'Premium', 0], [3, 'VIP', 0], [4, 'Premium', 5117], [4, 'VIP', 14933]], ordered=True)
