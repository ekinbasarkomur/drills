"""
3564. Seasonal Sales Analysis · Medium · https://leetcode.com/problems/seasonal-sales-analysis/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['product_id', 'product_name', 'category'], [[1, 'Warm Jacket', 'Apparel'], [2, 'Designer Jeans', 'Apparel'], [3, 'Cutting Board', 'Kitchen'], [4, 'Smart Speaker', 'Tech'], [5, 'Yoga Mat', 'Fitness']], {})
    sales = frame(['sale_id', 'product_id', 'sale_date', 'quantity', 'price'], [[1, 1, '2023-01-15', 5, 10.0], [2, 2, '2023-01-20', 4, 15.0], [3, 3, '2023-03-10', 3, 18.0], [4, 4, '2023-04-05', 1, 20.0], [5, 1, '2023-05-20', 2, 10.0], [6, 2, '2023-06-12', 4, 15.0], [7, 5, '2023-06-15', 5, 12.0], [8, 3, '2023-07-24', 2, 18.0], [9, 4, '2023-08-01', 5, 20.0], [10, 5, '2023-09-03', 3, 12.0], [11, 1, '2023-09-25', 6, 10.0], [12, 2, '2023-11-10', 4, 15.0], [13, 3, '2023-12-05', 6, 18.0], [14, 4, '2023-12-22', 3, 20.0], [15, 5, '2024-02-14', 2, 12.0]], {})
    check(seasonal_sales_analysis(products, sales), ['season', 'category', 'total_quantity', 'total_revenue'], [['Fall', 'Apparel', 10, 120.0], ['Spring', 'Kitchen', 3, 54.0], ['Summer', 'Tech', 5, 100.0], ['Winter', 'Apparel', 9, 110.0]], ordered=True)
