"""
1384. Total Sales Amount by Year · Hard · https://leetcode.com/problems/total-sales-amount-by-year/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def total_sales(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    product = frame(['product_id', 'product_name'], [[1, 'LC Phone '], [2, 'LC T-Shirt'], [3, 'LC Keychain']], {'product_id': 'Int64', 'product_name': 'object'})
    sales = frame(['product_id', 'period_start', 'period_end', 'average_daily_sales'], [[1, '2019-01-25', '2019-02-28', 100], [2, '2018-12-01', '2020-01-01', 10], [3, '2019-12-01', '2020-01-31', 1]], {'product_id': 'Int64', 'period_start': 'datetime64[ns]', 'period_end': 'datetime64[ns]', 'average_daily_sales': 'Int64'})
    check(total_sales(product, sales), ['product_id', 'product_name', 'report_year', 'total_amount'], [[1, 'LC Phone', 2019, 3500], [2, 'LC T-Shirt', 2018, 310], [2, 'LC T-Shirt', 2019, 3650], [2, 'LC T-Shirt', 2020, 10], [3, 'LC Keychain', 2019, 31], [3, 'LC Keychain', 2020, 31]], ordered=True)
