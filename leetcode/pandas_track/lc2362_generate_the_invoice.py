"""
2362. Generate the Invoice · Hard · https://leetcode.com/problems/generate-the-invoice/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'price'], [[1, 100], [2, 200]], {'product_id': 'Int64', 'price': 'Int64'})
    purchases = frame(['invoice_id', 'product_id', 'quantity'], [[1, 1, 2], [3, 2, 1], [2, 2, 3], [2, 1, 4], [4, 1, 10]], {'invoice_id': 'Int64', 'product_id': 'Int64', 'quantity': 'Int64'})
    check(generate_the_invoice(products, purchases), ['product_id', 'quantity', 'price'], [[2, 3, 600], [1, 4, 400]], ordered=False)
