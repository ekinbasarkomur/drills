"""
1777. Product's Price for Each Store · Easy · https://leetcode.com/problems/products-price-for-each-store/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'store', 'price'], [['0', 'store1', '95'], ['0', 'store3', '105'], ['0', 'store2', '100'], ['1', 'store1', '70'], ['1', 'store3', '80']], {'product_id': 'Int64', 'store': 'category', 'price': 'Int64'})
    check(products_price(products), ['product_id', 'store1', 'store2', 'store3'], [[0, 95, 100, 105], [1, 70, None, 80]], ordered=False)
