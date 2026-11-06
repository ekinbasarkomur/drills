"""
2324. Product Sales Analysis IV · Medium · https://leetcode.com/problems/product-sales-analysis-iv/
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
    sales = frame(['sale_id', 'product_id', 'user_id', 'quantity'], [[1, 1, 101, 10], [2, 3, 101, 7], [3, 1, 102, 9], [4, 2, 102, 6], [5, 3, 102, 10], [6, 1, 102, 6]], {'sale_id': 'Int64', 'product_id': 'Int64', 'user_id': 'Int64', 'quantity': 'Int64'})
    product = frame(['product_id', 'price'], [[1, 10], [2, 25], [3, 15]], {'product_id': 'Int64', 'price': 'Int64'})
    check(product_sales_analysis(sales, product), ['user_id', 'product_id'], [[101, 3], [102, 1], [102, 2], [102, 3]], ordered=False)
