"""
2701. Consecutive Transactions with Increasing Amounts · Hard · https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def consecutive_increasing_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['transaction_id', 'customer_id', 'transaction_date', 'amount'], [[1, 101, '2023-05-01', 100], [2, 101, '2023-05-02', 150], [3, 101, '2023-05-03', 200], [4, 102, '2023-05-01', 50], [5, 102, '2023-05-03', 100], [6, 102, '2023-05-04', 200], [7, 105, '2023-05-01', 100], [8, 105, '2023-05-02', 150], [9, 105, '2023-05-03', 200], [10, 105, '2023-05-04', 300], [11, 105, '2023-05-12', 250], [12, 105, '2023-05-13', 260], [13, 105, '2023-05-14', 270]], {'transaction_id': 'Int64', 'customer_id': 'Int64', 'transaction_date': 'datetime64[ns]', 'amount': 'Int64'})
    check(consecutive_increasing_transactions(transactions), ['customer_id', 'consecutive_start', 'consecutive_end'], [[101, '2023-05-01', '2023-05-03'], [105, '2023-05-01', '2023-05-04'], [105, '2023-05-12', '2023-05-14']], ordered=True)
