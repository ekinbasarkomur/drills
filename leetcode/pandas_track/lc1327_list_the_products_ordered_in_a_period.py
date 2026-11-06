"""
1327. List the Products Ordered in a Period · Easy · https://leetcode.com/problems/list-the-products-ordered-in-a-period/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'product_name', 'product_category'], [[1, 'Leetcode Solutions', 'Book'], [2, 'Jewels of Stringology', 'Book'], [3, 'HP', 'Laptop'], [4, 'Lenovo', 'Laptop'], [5, 'Leetcode Kit', 'T-shirt']], {'product_id': 'Int64', 'product_name': 'object', 'product_category': 'object'})
    orders = frame(['product_id', 'order_date', 'unit'], [[1, '2020-02-05', 60], [1, '2020-02-10', 70], [2, '2020-01-18', 30], [2, '2020-02-11', 80], [3, '2020-02-17', 2], [3, '2020-02-24', 3], [4, '2020-03-01', 20], [4, '2020-03-04', 30], [4, '2020-03-04', 60], [5, '2020-02-25', 50], [5, '2020-02-27', 50], [5, '2020-03-01', 50]], {'product_id': 'Int64', 'order_date': 'datetime64[ns]', 'unit': 'Int64'})
    check(list_products(products, orders), ['product_name', 'unit'], [['Leetcode Solutions', 130], ['Leetcode Kit', 100]], ordered=False)
