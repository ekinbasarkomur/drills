"""
1336. Number of Transactions per Visit · Hard · https://leetcode.com/problems/number-of-transactions-per-visit/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def draw_chart(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    visits = frame(['user_id', 'visit_date'], [[1, '2020-01-01'], [2, '2020-01-02'], [12, '2020-01-01'], [19, '2020-01-03'], [1, '2020-01-02'], [2, '2020-01-03'], [1, '2020-01-04'], [7, '2020-01-11'], [9, '2020-01-25'], [8, '2020-01-28']], {'user_id': 'Int64', 'visit_date': 'datetime64[ns]'})
    transactions = frame(['user_id', 'transaction_date', 'amount'], [[1, '2020-01-02', 120], [2, '2020-01-03', 22], [7, '2020-01-11', 232], [1, '2020-01-04', 7], [9, '2020-01-25', 33], [9, '2020-01-25', 66], [8, '2020-01-28', 1], [9, '2020-01-25', 99]], {'user_id': 'Int64', 'transaction_date': 'datetime64[ns]', 'amount': 'Int64'})
    check(draw_chart(visits, transactions), ['transactions_count', 'visits_count'], [[0, 4], [1, 5], [2, 0], [3, 1]], ordered=True)
