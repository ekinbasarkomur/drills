"""
2084. Drop Type 1 Orders for Customers With Type 0 Orders · Medium · https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'customer_id', 'order_type'], [[1, 1, 0], [2, 1, 0], [11, 2, 0], [12, 2, 1], [21, 3, 1], [22, 3, 0], [31, 4, 1], [32, 4, 1]], {'order_id': 'Int64', 'customer_id': 'Int64', 'order_type': 'Int64'})
    check(drop_specific_orders(orders), ['order_id', 'customer_id', 'order_type'], [[31, 4, 1], [32, 4, 1], [1, 1, 0], [2, 1, 0], [11, 2, 0], [22, 3, 0]], ordered=False)
