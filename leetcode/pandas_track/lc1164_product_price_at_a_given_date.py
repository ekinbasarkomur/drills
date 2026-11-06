"""
1164. Product Price at a Given Date · Medium · https://leetcode.com/problems/product-price-at-a-given-date/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'new_price', 'change_date'], [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']], {'product_id': 'Int64', 'new_price': 'Int64', 'change_date': 'datetime64[ns]'})
    check(price_at_given_date(products), ['product_id', 'price'], [[2, 50], [1, 35], [3, 10]], ordered=False)
