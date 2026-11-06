"""
1069. Product Sales Analysis II · Easy · https://leetcode.com/problems/product-sales-analysis-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sales = frame(['sale_id', 'product_id', 'year', 'quantity', 'price'], [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]], {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    product = frame(['product_id', 'product_name'], [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']], {'product_id': 'Int64', 'product_name': 'object'})
    check(sales_analysis(sales, product), ['product_id', 'total_quantity'], [[100, 22], [200, 15]], ordered=False)
