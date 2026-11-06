"""
1205. Monthly Transactions II · Medium · https://leetcode.com/problems/monthly-transactions-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['id', 'country', 'state', 'amount', 'trans_date'], [[101, 'US', 'approved', 1000, '2019-05-18'], [102, 'US', 'declined', 2000, '2019-05-19'], [103, 'US', 'approved', 3000, '2019-06-10'], [104, 'US', 'declined', 4000, '2019-06-13'], [105, 'US', 'approved', 5000, '2019-06-15']], {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})
    chargebacks = frame(['trans_id', 'trans_date'], [[102, '2019-05-29'], [101, '2019-06-30'], [105, '2019-09-18']], {'trans_id': 'Int64', 'trans_date': 'datetime64[ns]'})
    check(monthly_transactions(transactions, chargebacks), ['month', 'country', 'approved_count', 'approved_amount', 'chargeback_count', 'chargeback_amount'], [['2019-05', 'US', 1, 1000, 1, 2000], ['2019-06', 'US', 2, 8000, 1, 1000], ['2019-09', 'US', 0, 0, 1, 5000]], ordered=False)
