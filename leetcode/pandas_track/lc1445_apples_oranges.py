"""
1445. Apples & Oranges · Medium · https://leetcode.com/problems/apples-oranges/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sales = frame(['sale_date', 'fruit', 'sold_num'], [['2020-05-01', 'apples', 10], ['2020-05-01', 'oranges', 8], ['2020-05-02', 'apples', 15], ['2020-05-02', 'oranges', 15], ['2020-05-03', 'apples', 20], ['2020-05-03', 'oranges', 0], ['2020-05-04', 'apples', 15], ['2020-05-04', 'oranges', 16]], {'sale_date': 'datetime64[ns]', 'fruit': 'object', 'sold_num': 'Int64'})
    check(apples_oranges(sales), ['sale_date', 'diff'], [['2020-05-01', 2], ['2020-05-02', 0], ['2020-05-03', 20], ['2020-05-04', -1]], ordered=True)
