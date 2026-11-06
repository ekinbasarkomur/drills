"""
1677. Product's Worth Over Invoices · Easy · https://leetcode.com/problems/products-worth-over-invoices/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    product = frame(['product_id', 'name'], [[0, 'ham'], [1, 'bacon']], {'product_id': 'Int64', 'name': 'object'})
    invoice = frame(['invoice_id', 'product_id', 'rest', 'paid', 'canceled', 'refunded'], [[23, 0, 2, 0, 5, 0], [12, 0, 0, 4, 0, 3], [1, 1, 1, 1, 0, 1], [2, 1, 1, 0, 1, 1], [3, 1, 0, 1, 1, 1], [4, 1, 1, 1, 1, 0]], {'invoice_id': 'Int64', 'product_id': 'Int64', 'rest': 'Int64', 'paid': 'Int64', 'canceled': 'Int64', 'refunded': 'Int64'})
    check(analyze_products(product, invoice), ['name', 'rest', 'paid', 'canceled', 'refunded'], [['bacon', 3, 3, 3, 3], ['ham', 2, 4, 5, 3]], ordered=True)
