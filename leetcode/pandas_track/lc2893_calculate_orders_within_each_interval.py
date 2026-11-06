"""
2893. Calculate Orders Within Each Interval · Medium · https://leetcode.com/problems/calculate-orders-within-each-interval/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_runs(orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['minute', 'order_count'], [[1, 0], [2, 2], [3, 4], [4, 6], [5, 1], [6, 4], [7, 1], [8, 2], [9, 4], [10, 1], [11, 4], [12, 6]], {'minute': 'Int64', 'order_count': 'Int64'})
    check(calculate_runs(orders), ['interval_no', 'total_orders'], [[1, 17], [2, 18]], ordered=True)
