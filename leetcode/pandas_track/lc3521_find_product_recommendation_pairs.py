"""
3521. Find Product Recommendation Pairs · Medium · https://leetcode.com/problems/find-product-recommendation-pairs/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    product_purchases = frame(['user_id', 'product_id', 'quantity'], [[1, 101, 2], [1, 102, 1], [1, 103, 3], [2, 101, 1], [2, 102, 5], [2, 104, 1], [3, 101, 2], [3, 103, 1], [3, 105, 4], [4, 101, 1], [4, 102, 1], [4, 103, 2], [4, 104, 3], [5, 102, 2], [5, 104, 1]], {})
    product_info = frame(['product_id', 'category', 'price'], [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Clothing', 35], [104, 'Kitchen', 50], [105, 'Sports', 75]], {})
    check(find_product_recommendation_pairs(product_purchases, product_info), ['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count'], [[101, 102, 'Electronics', 'Books', 3], [101, 103, 'Electronics', 'Clothing', 3], [102, 104, 'Books', 'Kitchen', 3]], ordered=True)
