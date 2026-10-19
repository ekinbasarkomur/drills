"""
183. Customers Who Never Order · Easy · https://leetcode.com/problems/customers-who-never-order/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['id', 'name'], [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']], {'id': 'Int64', 'name': 'object'})
    orders = frame(['id', 'customerId'], [[1, 3], [2, 1]], {'id': 'Int64', 'customerId': 'Int64'})
    check(find_customers(customers, orders), ['Customers'], [['Henry'], ['Max']], ordered=False)
