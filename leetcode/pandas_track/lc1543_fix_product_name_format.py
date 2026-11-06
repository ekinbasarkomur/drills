"""
1543. Fix Product Name Format · Easy · https://leetcode.com/problems/fix-product-name-format/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sales = frame(['sale_id', 'product_name', 'sale_date'], [[1, 'LCPHONE', '2000-01-16'], [2, 'LCPhone', '2000-01-17'], [3, 'LcPhOnE', '2000-02-18'], [4, 'LCKeyCHAiN', '2000-02-19'], [5, 'LCKeyChain', '2000-02-28'], [6, 'Matryoshka', '2000-03-31']], {'sale_id': 'Int64', 'product_name': 'object', 'sale_date': 'datetime64[ns]'})
    check(fix_name_format(sales), ['product_name', 'sale_date', 'total'], [['lckeychain', '2000-02', 2], ['lcphone', '2000-01', 2], ['lcphone', '2000-02', 1], ['matryoshka', '2000-03', 1]], ordered=True)
