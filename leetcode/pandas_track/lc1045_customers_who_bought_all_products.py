"""
1045. Customers Who Bought All Products · Medium · https://leetcode.com/problems/customers-who-bought-all-products/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customer = frame(['customer_id', 'product_key'], [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]], {'customer_id': 'Int64', 'product_key': 'Int64'})
    product = frame(['product_key'], [[5], [6]], {'product_key': 'Int64'})
    check(find_customers(customer, product), ['customer_id'], [[1], [3]], ordered=False)
