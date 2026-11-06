"""
1082. Sales Analysis I · Easy · https://leetcode.com/problems/sales-analysis-i/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    product = frame(['product_id', 'product_name', 'unit_price'], [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]], {'product_id': 'Int64', 'product_name': 'object', 'unit_price': 'Int64'})
    sales = frame(['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price'], [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]], {'seller_id': 'Int64', 'product_id': 'Int64', 'buyer_id': 'Int64', 'sale_date': 'datetime64[ns]', 'quantity': 'Int64', 'price': 'Int64'})
    check(sales_analysis(product, sales), ['seller_id'], [[1], [3]], ordered=False)
