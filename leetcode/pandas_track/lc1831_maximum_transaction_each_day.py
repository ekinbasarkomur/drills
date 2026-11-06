"""
1831. Maximum Transaction Each Day · Medium · https://leetcode.com/problems/maximum-transaction-each-day/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['transaction_id', 'day', 'amount'], [[8, '2021-4-3 15:57:28', 57], [9, '2021-4-28 08:47:25', 21], [1, '2021-4-29 13:28:30', 58], [5, '2021-4-28 16:39:59', 40], [6, '2021-4-29 23:39:28', 58]], {'transaction_id': 'Int64', 'day': 'datetime64[ns]', 'amount': 'Int64'})
    check(find_maximum_transaction(transactions), ['transaction_id'], [[1], [5], [6], [8]], ordered=True)
