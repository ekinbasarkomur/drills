"""
3554. Find Category Recommendation Pairs · Hard · https://leetcode.com/problems/find-category-recommendation-pairs/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    product_purchases = frame(['user_id', 'product_id', 'quantity'], [[1, 101, 2], [1, 102, 1], [1, 201, 3], [1, 301, 1], [2, 101, 1], [2, 102, 2], [2, 103, 1], [2, 201, 5], [3, 101, 2], [3, 103, 1], [3, 301, 4], [3, 401, 2], [4, 101, 1], [4, 201, 3], [4, 301, 1], [4, 401, 2], [5, 102, 2], [5, 103, 1], [5, 201, 2], [5, 202, 3]], {})
    product_info = frame(['product_id', 'category', 'price'], [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Books', 35], [201, 'Clothing', 45], [202, 'Clothing', 60], [301, 'Sports', 75], [401, 'Kitchen', 50]], {})
    check(find_category_recommendation_pairs(product_purchases, product_info), ['category1', 'category2', 'customer_count'], [['Books', 'Clothing', 3], ['Books', 'Electronics', 3], ['Clothing', 'Electronics', 3], ['Electronics', 'Sports', 3]], ordered=True)
