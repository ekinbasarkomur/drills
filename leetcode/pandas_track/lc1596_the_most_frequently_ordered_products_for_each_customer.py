"""
1596. The Most Frequently Ordered Products for Each Customer · Medium · https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'name'], [[1, 'Alice'], [2, 'Bob'], [3, 'Tom'], [4, 'Jerry'], [5, 'John']], {'customer_id': 'Int64', 'name': 'object'})
    orders = frame(['order_id', 'order_date', 'customer_id', 'product_id'], [[1, '2020-07-31', 1, 1], [2, '2020-7-30', 2, 2], [3, '2020-08-29', 3, 3], [4, '2020-07-29', 4, 1], [5, '2020-06-10', 1, 2], [6, '2020-08-01', 2, 1], [7, '2020-08-01', 3, 3], [8, '2020-08-03', 1, 2], [9, '2020-08-07', 2, 3], [10, '2020-07-15', 1, 2]], {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'product_id': 'Int64'})
    products = frame(['product_id', 'product_name', 'price'], [[1, 'keyboard', 120], [2, 'mouse', 80], [3, 'screen', 600], [4, 'hard disk', 450]], {'product_id': 'Int64', 'product_name': 'object', 'price': 'Int64'})
    check(most_frequently_products(customers, orders, products), ['customer_id', 'product_id', 'product_name'], [[1, 2, 'mouse'], [2, 1, 'keyboard'], [2, 2, 'mouse'], [2, 3, 'screen'], [3, 3, 'screen'], [4, 1, 'keyboard']], ordered=False)
