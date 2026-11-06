"""
1607. Sellers With No Sales · Easy · https://leetcode.com/problems/sellers-with-no-sales/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customer = frame(['customer_id', 'customer_name'], [[101, 'Alice'], [102, 'Bob'], [103, 'Charlie']], {'customer_id': 'Int64', 'customer_name': 'object'})
    orders = frame(['order_id', 'sale_date', 'order_cost', 'customer_id', 'seller_id'], [[1, '2020-03-01', 1500, 101, 1], [2, '2020-05-25', 2400, 102, 2], [3, '2019-05-25', 800, 101, 3], [4, '2020-09-13', 1000, 103, 2], [5, '2019-02-11', 700, 101, 2]], {'order_id': 'Int64', 'sale_date': 'datetime64[ns]', 'order_cost': 'Int64', 'customer_id': 'Int64', 'seller_id': 'Int64'})
    seller = frame(['seller_id', 'seller_name'], [[1, 'Daniel'], [2, 'Elizabeth'], [3, 'Frank']], {'seller_id': 'Int64', 'seller_name': 'object'})
    check(sellers_with_no_sales(customer, orders, seller), ['seller_name'], [['Frank']], ordered=True)
