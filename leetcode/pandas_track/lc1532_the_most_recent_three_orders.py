"""
1532. The Most Recent Three Orders · Medium · https://leetcode.com/problems/the-most-recent-three-orders/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'name'], [[1, 'Winston'], [2, 'Jonathan'], [3, 'Annabelle'], [4, 'Marwan'], [5, 'Khaled']], {'customer_id': 'Int64', 'name': 'object'})
    orders = frame(['order_id', 'order_date', 'customer_id', 'cost'], [[1, '2020-07-31', 1, 30], [2, '2020-7-30', 2, 40], [3, '2020-07-31', 3, 70], [4, '2020-07-29', 4, 100], [5, '2020-06-10', 1, 1010], [6, '2020-08-01', 2, 102], [7, '2020-08-01', 3, 111], [8, '2020-08-03', 1, 99], [9, '2020-08-07', 2, 32], [10, '2020-07-15', 1, 2]], {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'cost': 'Int64'})
    check(recent_three_orders(customers, orders), ['customer_name', 'customer_id', 'order_id', 'order_date'], [['Annabelle', 3, 7, '2020-08-01'], ['Annabelle', 3, 3, '2020-07-31'], ['Jonathan', 2, 9, '2020-08-07'], ['Jonathan', 2, 6, '2020-08-01'], ['Jonathan', 2, 2, '2020-07-30'], ['Marwan', 4, 4, '2020-07-29'], ['Winston', 1, 8, '2020-08-03'], ['Winston', 1, 1, '2020-07-31'], ['Winston', 1, 10, '2020-07-15']], ordered=True)
