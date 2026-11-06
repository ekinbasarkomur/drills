"""
1398. Customers Who Bought Products A and B but Not C · Medium · https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'customer_name'], [[1, 'Daniel'], [2, 'Diana'], [3, 'Elizabeth'], [4, 'Jhon']], {'customer_id': 'Int64', 'customer_name': 'object'})
    orders = frame(['order_id', 'customer_id', 'product_name'], [[10, 1, 'A'], [20, 1, 'B'], [30, 1, 'D'], [40, 1, 'C'], [50, 2, 'A'], [60, 3, 'A'], [70, 3, 'B'], [80, 3, 'D'], [90, 4, 'C']], {'order_id': 'Int64', 'customer_id': 'Int64', 'product_name': 'object'})
    check(find_customers(customers, orders), ['customer_id', 'customer_name'], [[3, 'Elizabeth']], ordered=True)
