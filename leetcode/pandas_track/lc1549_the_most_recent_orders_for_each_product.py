"""
1549. The Most Recent Orders for Each Product · Medium · https://leetcode.com/problems/the-most-recent-orders-for-each-product/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'name'], [[1, 'Winston'], [2, 'Jonathan'], [3, 'Annabelle'], [4, 'Marwan'], [5, 'Khaled']], {'customer_id': 'Int64', 'name': 'object'})
    orders = frame(['order_id', 'order_date', 'customer_id', 'product_id'], [[1, '2020-07-31', 1, 1], [2, '2020-7-30', 2, 2], [3, '2020-08-29', 3, 3], [4, '2020-07-29', 4, 1], [5, '2020-06-10', 1, 2], [6, '2020-08-01', 2, 1], [7, '2020-08-01', 3, 1], [8, '2020-08-03', 1, 2], [9, '2020-08-07', 2, 3], [10, '2020-07-15', 1, 2]], {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'product_id': 'Int64'})
    products = frame(['product_id', 'product_name', 'price'], [[1, 'keyboard', 120], [2, 'mouse', 80], [3, 'screen', 600], [4, 'hard disk', 450]], {'product_id': 'Int64', 'product_name': 'object', 'price': 'Int64'})
    check(most_recent_orders(customers, orders, products), ['product_name', 'product_id', 'order_id', 'order_date'], [['keyboard', 1, 6, '2020-08-01'], ['keyboard', 1, 7, '2020-08-01'], ['mouse', 2, 8, '2020-08-03'], ['screen', 3, 3, '2020-08-29']], ordered=True)
