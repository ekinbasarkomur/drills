"""
1070. Product Sales Analysis III · Medium · https://leetcode.com/problems/product-sales-analysis-iii/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sales = frame(['sale_id', 'product_id', 'year', 'quantity', 'price'], [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]], {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    check(sales_analysis(sales), ['product_id', 'first_year', 'quantity', 'price'], [[100, 2008, 10, 5000], [200, 2011, 15, 9000]], ordered=False)
