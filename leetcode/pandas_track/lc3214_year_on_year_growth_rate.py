"""
3214. Year on Year Growth Rate · Hard · https://leetcode.com/problems/year-on-year-growth-rate/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_transactions = frame(['transaction_id', 'product_id', 'spend', 'transaction_date'], [[1341, 123424, 1500.6, '2019-12-31 12:00:00'], [1423, 123424, 1000.2, '2020-12-31 12:00:00'], [1623, 123424, 1246.44, '2021-12-31 12:00:00'], [1322, 123424, 2145.32, '2022-12-31 12:00:00']], {})
    check(calculate_yoy_growth(user_transactions), ['year', 'product_id', 'curr_year_spend', 'prev_year_spend', 'yoy_rate'], [[2019, 123424, 1500.6, None, None], [2020, 123424, 1000.2, 1500.6, -33.35], [2021, 123424, 1246.44, 1000.2, 24.62], [2022, 123424, 2145.32, 1246.44, 72.12]], ordered=True)
