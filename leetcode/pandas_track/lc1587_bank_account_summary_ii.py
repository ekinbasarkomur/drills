"""
1587. Bank Account Summary II · Easy · https://leetcode.com/problems/bank-account-summary-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['account', 'name'], [[900001, 'Alice'], [900002, 'Bob'], [900003, 'Charlie']], {'account': 'Int64', 'name': 'object'})
    transactions = frame(['trans_id', 'account', 'amount', 'transacted_on'], [[1, 900001, 7000, '2020-08-01'], [2, 900001, 7000, '2020-09-01'], [3, 900001, -3000, '2020-09-02'], [4, 900002, 1000, '2020-09-12'], [5, 900003, 6000, '2020-08-07'], [6, 900003, 6000, '2020-09-07'], [7, 900003, -4000, '2020-09-11']], {'trans_id': 'Int64', 'account': 'Int64', 'amount': 'Int64', 'transacted_on': 'datetime64[ns]'})
    check(account_summary(users, transactions), ['name', 'balance'], [['Alice', 11000]], ordered=False)
