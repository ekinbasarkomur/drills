"""
1193. Monthly Transactions I · Medium · https://leetcode.com/problems/monthly-transactions-i/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['id', 'country', 'state', 'amount', 'trans_date'], [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']], {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})
    check(monthly_transactions(transactions), ['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount'], [['2018-12', 'US', 2, 1, 3000, 1000], ['2019-01', 'US', 1, 1, 2000, 2000], ['2019-01', 'DE', 1, 1, 2000, 2000]], ordered=False)
