"""
1068. Product Sales Analysis I · Easy · https://leetcode.com/problems/product-sales-analysis-i/
Plan: Paralel hat · SQL

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
    check(sales_analysis(sales, product), ['product_name', 'year', 'price'], [['Nokia', 2008, 5000], ['Nokia', 2009, 5000], ['Apple', 2011, 9000]], ordered=False)
