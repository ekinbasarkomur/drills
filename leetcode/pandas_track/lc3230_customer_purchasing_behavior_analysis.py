"""
3230. Customer Purchasing Behavior Analysis · Medium · https://leetcode.com/problems/customer-purchasing-behavior-analysis/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def analyze_customer_behavior(transactions: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    transactions = frame(['transaction_id', 'customer_id', 'product_id', 'transaction_date', 'amount'], [[1, 101, 1, '2023-01-01', 100.0], [2, 101, 2, '2023-01-15', 150.0], [3, 102, 1, '2023-01-01', 100.0], [4, 102, 3, '2023-01-22', 200.0], [5, 101, 3, '2023-02-10', 200.0]], {})
    products = frame(['product_id', 'category', 'price'], [[1, 'A', 100.0], [2, 'B', 150.0], [3, 'C', 200.0]], {})
    check(analyze_customer_behavior(transactions, products), ['customer_id', 'total_amount', 'transaction_count', 'unique_categories', 'avg_transaction_amount', 'top_category', 'loyalty_score'], [[101, 450.0, 3, 3, 150.0, 'C', 34.5], [102, 300.0, 2, 2, 150.0, 'C', 23.0]], ordered=True)
