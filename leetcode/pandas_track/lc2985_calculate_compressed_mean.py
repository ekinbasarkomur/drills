"""
2985. Calculate Compressed Mean · Easy · https://leetcode.com/problems/calculate-compressed-mean/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'item_count', 'order_occurrences'], [[10, 1, 500], [11, 2, 1000], [12, 3, 800], [13, 4, 1000]], {'order_id': 'Int64', 'item_count': 'Int64', 'order_occurrences': 'Int64'})
    check(compressed_mean(orders), ['average_items_per_order'], [[2.7]], ordered=False)
