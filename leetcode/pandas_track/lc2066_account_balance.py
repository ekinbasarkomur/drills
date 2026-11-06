"""
2066. Account Balance · Medium · https://leetcode.com/problems/account-balance/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['account_id', 'day', 'type', 'amount'], [[1, '2021-11-07', 'Deposit', 2000], [1, '2021-11-09', 'Withdraw', 1000], [1, '2021-11-11', 'Deposit', 3000], [2, '2021-12-07', 'Deposit', 7000], [2, '2021-12-12', 'Withdraw', 7000]], {'account_id': 'Int64', 'day': 'datetime64[ns]', 'type': 'object', 'amount': 'Int64'})
    check(account_balance(transactions), ['account_id', 'day', 'balance'], [[1, '2021-11-07', 2000], [1, '2021-11-09', 1000], [1, '2021-11-11', 4000], [2, '2021-12-07', 7000], [2, '2021-12-12', 0]], ordered=True)
