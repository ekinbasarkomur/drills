"""
586. Customer Placing the Largest Number of Orders · Easy · https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_number', 'customer_number'], [[1, 1], [2, 2], [3, 3], [4, 3]], {'order_number': 'Int64', 'customer_number': 'Int64'})
    check(largest_orders(orders), ['customer_number'], [[3]], ordered=False)
