"""
2292. Products With Three or More Orders in Two Consecutive Years · Medium · https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'product_id', 'quantity', 'purchase_date'], [[1, 1, 7, '2020-03-16'], [2, 1, 4, '2020-12-02'], [3, 1, 7, '2020-05-10'], [4, 1, 6, '2021-12-23'], [5, 1, 5, '2021-05-21'], [6, 1, 6, '2021-10-11'], [7, 2, 6, '2022-10-11']], {'order_id': 'Int64', 'product_id': 'Int64', 'quantity': 'Int64', 'purchase_date': 'datetime64[ns]'})
    check(find_valid_products(orders), ['product_id'], [[1]], ordered=False)
