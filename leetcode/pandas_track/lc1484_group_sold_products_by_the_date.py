"""
1484. Group Sold Products By The Date · Easy · https://leetcode.com/problems/group-sold-products-by-the-date/
Plan: 30 Days of Pandas · Gün 24 · Data Aggregation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    activities = frame(['sell_date', 'product'], [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']], {'sell_date': 'datetime64[ns]', 'product': 'object'})
    check(categorize_products(activities), ['sell_date', 'num_sold', 'products'], [['2020-05-30', 3, 'Basketball,Headphone,T-shirt'], ['2020-06-01', 2, 'Bible,Pencil'], ['2020-06-02', 1, 'Mask']], ordered=True)
