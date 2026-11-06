"""
2329. Product Sales Analysis V · Easy · https://leetcode.com/problems/product-sales-analysis-v/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sales = frame(['sale_id', 'product_id', 'user_id', 'quantity'], [[1, 1, 101, 10], [2, 2, 101, 1], [3, 3, 102, 3], [4, 3, 102, 2], [5, 2, 103, 3]], {'sale_id': 'Int64', 'product_id': 'Int64', 'user_id': 'Int64', 'quantity': 'Int64'})
    product = frame(['product_id', 'price'], [[1, 10], [2, 25], [3, 15]], {'product_id': 'Int64', 'price': 'Int64'})
    check(product_sales_analysis(sales, product), ['user_id', 'spending'], [[101, 125], [102, 75], [103, 75]], ordered=True)
