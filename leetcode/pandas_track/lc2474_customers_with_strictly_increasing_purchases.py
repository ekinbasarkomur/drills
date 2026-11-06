"""
2474. Customers With Strictly Increasing Purchases · Hard · https://leetcode.com/problems/customers-with-strictly-increasing-purchases/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_specific_customers(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'customer_id', 'order_date', 'price'], [[1, 1, '2019-07-01', 1100], [2, 1, '2019-11-01', 1200], [3, 1, '2020-05-26', 3000], [4, 1, '2021-08-31', 3100], [5, 1, '2022-12-07', 4700], [6, 2, '2015-01-01', 700], [7, 2, '2017-11-07', 1000], [8, 3, '2017-01-01', 900], [9, 3, '2018-11-07', 900]], {'order_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]', 'price': 'Int64'})
    check(find_specific_customers(orders), ['customer_id'], [[1]], ordered=False)
