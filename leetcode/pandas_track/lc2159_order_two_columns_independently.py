"""
2159. Order Two Columns Independently · Medium · https://leetcode.com/problems/order-two-columns-independently/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    data = frame(['first_col', 'second_col'], [[4, 2], [2, 3], [3, 1], [1, 4]], {'first_col': 'Int64', 'second_col': 'Int64'})
    check(order_two_columns(data), ['first_col', 'second_col'], [[1, 4], [2, 3], [3, 2], [4, 1]], ordered=False)
