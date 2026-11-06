"""
3415. Find Products with Three Consecutive Digits  · Easy · https://leetcode.com/problems/find-products-with-three-consecutive-digits/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'name'], [[1, 'ABC123XYZ'], [2, 'A12B34C'], [3, 'Product56789'], [4, 'NoDigitsHere'], [5, '789Product'], [6, 'Item003Description'], [7, 'Product12X34']], {})
    check(find_products(products), ['product_id', 'name'], [[1, 'ABC123XYZ'], [5, '789Product'], [6, 'Item003Description']], ordered=True)
