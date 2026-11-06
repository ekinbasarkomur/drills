"""
1581. Customer Who Visited but Did Not Make Any Transactions · Easy · https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    visits = frame(['visit_id', 'customer_id'], [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]], {'visit_id': 'Int64', 'customer_id': 'Int64'})
    transactions = frame(['transaction_id', 'visit_id', 'amount'], [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]], {'transaction_id': 'Int64', 'visit_id': 'Int64', 'amount': 'Int64'})
    check(find_customers(visits, transactions), ['customer_id', 'count_no_trans'], [[54, 2], [30, 1], [96, 1]], ordered=False)
