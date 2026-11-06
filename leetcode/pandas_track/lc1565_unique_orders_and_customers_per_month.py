"""
1565. Unique Orders and Customers Per Month · Easy · https://leetcode.com/problems/unique-orders-and-customers-per-month/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'order_date', 'customer_id', 'invoice'], [[1, '2020-09-15', 1, 30], [2, '2020-09-17', 2, 90], [3, '2020-10-06', 3, 20], [4, '2020-10-20', 3, 21], [5, '2020-11-10', 1, 10], [6, '2020-11-21', 2, 15], [7, '2020-12-01', 4, 55], [8, '2020-12-03', 4, 77], [9, '2021-01-07', 3, 31], [10, '2021-01-15', 2, 20]], {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'invoice': 'Int64'})
    check(unique_orders_and_customers(orders), ['month', 'order_count', 'customer_count'], [['2020-09', 2, 2], ['2020-10', 1, 1], ['2020-12', 2, 1], ['2021-01', 1, 1]], ordered=False)
