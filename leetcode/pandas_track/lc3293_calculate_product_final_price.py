"""
3293. Calculate Product Final Price · Medium · https://leetcode.com/problems/calculate-product-final-price/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'category', 'price'], [[1, 'Electronics', 1000], [2, 'Clothing', 50], [3, 'Electronics', 1200], [4, 'Home', 500]], {})
    discounts = frame(['category', 'discount'], [['Electronics', 10], ['Clothing', 20]], {})
    check(calculate_final_prices(products, discounts), ['product_id', 'final_price', 'category'], [[1, 900, 'Electronics'], [2, 40, 'Clothing'], [3, 1080, 'Electronics'], [4, 500, 'Home']], ordered=True)
