"""
1479. Sales by Day of the Week · Hard · https://leetcode.com/problems/sales-by-day-of-the-week/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sales_by_day(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    orders = frame(['order_id', 'customer_id', 'order_date', 'item_id', 'quantity'], [[1, 1, '2020-06-01', 1, 10], [2, 1, '2020-06-08', 2, 10], [3, 2, '2020-06-02', 1, 5], [4, 3, '2020-06-03', 3, 5], [5, 4, '2020-06-04', 4, 1], [6, 4, '2020-06-05', 5, 5], [7, 5, '2020-06-05', 1, 10], [8, 5, '2020-06-14', 4, 5], [9, 5, '2020-06-21', 3, 5]], {'order_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]', 'item_id': 'object', 'quantity': 'Int64'})
    items = frame(['item_id', 'item_name', 'item_category'], [[1, 'LC Alg. Book', 'Book'], [2, 'LC DB. Book', 'Book'], [3, 'LC SmarthPhone', 'Phone'], [4, 'LC Phone 2020', 'Phone'], [5, 'LC SmartGlass', 'Glasses'], [6, 'LC T-Shirt XL', 'T-shirt']], {'item_id': 'object', 'item_name': 'object', 'item_category': 'object'})
    check(sales_by_day(orders, items), ['Category', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], [['Book', 20, 5, 0, 0, 10, 0, 0], ['Glasses', 0, 0, 0, 0, 5, 0, 0], ['Phone', 0, 0, 5, 1, 0, 0, 10], ['T-Shirt', 0, 0, 0, 0, 0, 0, 0]], ordered=True)
