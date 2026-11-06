"""
1251. Average Selling Price · Easy · https://leetcode.com/problems/average-selling-price/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    prices = frame(['product_id', 'start_date', 'end_date', 'price'], [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]], {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
    units_sold = frame(['product_id', 'purchase_date', 'units'], [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]], {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})
    check(average_selling_price(prices, units_sold), ['product_id', 'average_price'], [[1, 6.96], [2, 16.96]], ordered=False)
