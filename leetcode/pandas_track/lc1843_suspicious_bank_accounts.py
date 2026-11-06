"""
1843. Suspicious Bank Accounts · Medium · https://leetcode.com/problems/suspicious-bank-accounts/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    accounts = frame(['account_id', 'max_income'], [[3, 21000], [4, 10400]], {'account_id': 'Int64', 'max_income': 'Int64'})
    transactions = frame(['transaction_id', 'account_id', 'type', 'amount', 'day'], [[2, 3, 'Creditor', 107100, '2021-06-02 11:38:14'], [4, 4, 'Creditor', 10400, '2021-06-20 12:39:18'], [11, 4, 'Debtor', 58800, '2021-07-23 12:41:55'], [1, 4, 'Creditor', 49300, '2021-05-03 16:11:04'], [15, 3, 'Debtor', 75500, '2021-05-23 14:40:20'], [10, 3, 'Creditor', 102100, '2021-06-15 10:37:16'], [14, 4, 'Creditor', 56300, '2021-07-21 12:12:25'], [19, 4, 'Debtor', 101100, '2021-05-09 15:21:49'], [8, 3, 'Creditor', 64900, '2021-07-26 15:09:56'], [7, 3, 'Creditor', 90900, '2021-06-14 11:23:07']], {'transaction_id': 'Int64', 'account_id': 'Int64', 'type': 'object', 'amount': 'Int64', 'day': 'datetime64[ns]'})
    check(suspicious_bank_accounts(accounts, transactions), ['account_id'], [[3]], ordered=False)
