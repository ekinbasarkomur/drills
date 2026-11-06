"""
3220. Odd and Even Transactions · Medium · https://leetcode.com/problems/odd-and-even-transactions/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['transaction_id', 'amount', 'transaction_date'], [[1, 150, '2024-07-01'], [2, 200, '2024-07-01'], [3, 75, '2024-07-01'], [4, 300, '2024-07-02'], [5, 50, '2024-07-02'], [6, 120, '2024-07-03']], {})
    check(sum_daily_odd_even(transactions), ['transaction_date', 'odd_sum', 'even_sum'], [['2024-07-01', 75, 350], ['2024-07-02', 0, 350], ['2024-07-03', 0, 120]], ordered=True)
