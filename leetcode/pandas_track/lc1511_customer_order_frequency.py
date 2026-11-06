"""
1511. Customer Order Frequency · Easy · https://leetcode.com/problems/customer-order-frequency/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'name', 'country'], [[1, 'Winston', 'USA'], [2, 'Jonathan', 'Peru'], [3, 'Moustafa', 'Egypt']], {'customer_id': 'Int64', 'name': 'object', 'country': 'object'})
    product = frame(['product_id', 'description', 'price'], [[10, 'LC Phone', 300], [20, 'LC T-Shirt', 10], [30, 'LC Book', 45], [40, 'LC Keychain', 2]], {'product_id': 'Int64', 'description': 'object', 'price': 'Int64'})
    orders = frame(['order_id', 'customer_id', 'product_id', 'order_date', 'quantity'], [[1, 1, 10, '2020-06-10', 1], [2, 1, 20, '2020-07-01', 1], [3, 1, 30, '2020-07-08', 2], [4, 2, 10, '2020-06-15', 2], [5, 2, 40, '2020-07-01', 10], [6, 3, 20, '2020-06-24', 2], [7, 3, 30, '2020-06-25', 2], [9, 3, 30, '2020-05-08', 3]], {'order_id': 'Int64', 'customer_id': 'Int64', 'product_id': 'Int64', 'order_date': 'datetime64[ns]', 'quantity': 'Int64'})
    check(customer_order_frequency(customers, product, orders), ['customer_id', 'name'], [[1, 'Winston']], ordered=False)
