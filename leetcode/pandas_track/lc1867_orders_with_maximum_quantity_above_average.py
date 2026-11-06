"""
1867. Orders With Maximum Quantity Above Average · Medium · https://leetcode.com/problems/orders-with-maximum-quantity-above-average/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders_details = frame(['order_id', 'product_id', 'quantity'], [[1, 1, 12], [1, 2, 10], [1, 3, 15], [2, 1, 8], [2, 4, 4], [2, 5, 6], [3, 3, 5], [3, 4, 18], [4, 5, 2], [4, 6, 8], [5, 7, 9], [5, 8, 9], [3, 9, 20], [2, 9, 4]], {'order_id': 'Int64', 'product_id': 'Int64', 'quantity': 'Int64'})
    check(orders_above_average(orders_details), ['order_id'], [[1], [3]], ordered=False)
