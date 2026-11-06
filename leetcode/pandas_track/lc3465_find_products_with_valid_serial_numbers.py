"""
3465. Find Products with Valid Serial Numbers · Easy · https://leetcode.com/problems/find-products-with-valid-serial-numbers/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'product_name', 'description'], [[1, 'Widget A', 'This is a sample product with SN1234-5678'], [2, 'Widget B', 'A product with serial SN9876-1234 in the description'], [3, 'Widget C', 'Product SN1234-56789 is available now'], [4, 'Widget D', 'No serial number here'], [5, 'Widget E', 'Check out SN4321-8765 in this description']], {})
    check(find_valid_serial_products(products), ['product_id', 'product_name', 'description'], [[1, 'Widget A', 'This is a sample product with SN1234-5678'], [2, 'Widget B', 'A product with serial SN9876-1234 in the description'], [5, 'Widget E', 'Check out SN4321-8765 in this description']], ordered=True)
