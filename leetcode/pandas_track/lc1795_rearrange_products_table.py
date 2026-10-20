"""
1795. Rearrange Products Table · Easy · https://leetcode.com/problems/rearrange-products-table/
Plan: 30 Days of Pandas · Gün 15 · Data Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'store1', 'store2', 'store3'], [[0, 95, 100, 105], [1, 70, None, 80]], {'product_id': 'Int64', 'store1': 'Int64', 'store2': 'Int64', 'store3': 'Int64'})
    check(rearrange_products_table(products), ['product_id', 'store', 'price'], [[0, 'store1', 95], [0, 'store2', 100], [0, 'store3', 105], [1, 'store1', 70], [1, 'store3', 80]], ordered=False)
