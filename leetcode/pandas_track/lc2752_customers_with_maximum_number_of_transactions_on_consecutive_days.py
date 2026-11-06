"""
2752. Customers with Maximum Number of Transactions on Consecutive Days · Hard · https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['transaction_id', 'customer_id', 'transaction_date', 'amount'], [[1, 101, '2023-05-01', 100], [2, 101, '2023-05-02', 150], [3, 101, '2023-05-03', 200], [4, 102, '2023-05-01', 50], [5, 102, '2023-05-03', 100], [6, 102, '2023-05-04', 200], [7, 105, '2023-05-01', 100], [8, 105, '2023-05-02', 150], [9, 105, '2023-05-03', 200]], {'transaction_id': 'Int64', 'customer_id': 'Int64', 'transaction_date': 'datetime64[ns]', 'amount': 'Int64'})
    check(find_customers(transactions), ['customer_id'], [[101], [105]], ordered=False)
