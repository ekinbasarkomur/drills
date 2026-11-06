"""
1555. Bank Account Summary · Medium · https://leetcode.com/problems/bank-account-summary/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'user_name', 'credit'], [[1, 'Moustafa', 100], [2, 'Jonathan', 200], [3, 'Winston', 10000], [4, 'Luis', 800]], {'user_id': 'Int64', 'user_name': 'object', 'credit': 'Int64'})
    transactions = frame(['trans_id', 'paid_by', 'paid_to', 'amount', 'transacted_on'], [[1, 1, 3, 400, '2020-08-01'], [2, 3, 2, 500, '2020-08-02'], [3, 2, 1, 200, '2020-08-03']], {'trans_id': 'Int64', 'paid_by': 'Int64', 'paid_to': 'Int64', 'amount': 'Int64', 'transacted_on': 'datetime64[ns]'})
    check(bank_account_summary(users, transactions), ['user_id', 'user_name', 'credit', 'credit_limit_breached'], [[1, 'Moustafa', -100, 'Yes'], [2, 'Jonathan', 500, 'No'], [3, 'Winston', 9900, 'No'], [4, 'Luis', 800, 'No']], ordered=False)
