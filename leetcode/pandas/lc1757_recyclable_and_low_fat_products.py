"""
1757. Recyclable and Low Fat Products · Easy · https://leetcode.com/problems/recyclable-and-low-fat-products/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'low_fats', 'recyclable'], [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']], {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})
    check(find_products(products), ['product_id'], [[1], [3]], ordered=False)
