"""
2388. Change Null Values in a Table to the Previous Value · Medium · https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    coffee_shop = frame(['id', 'drink'], [[9, 'Rum and Coke'], [6, None], [7, None], [3, 'St Germain Spritz'], [1, 'Orange Margarita'], [2, None]], {'id': 'Int64', 'drink': 'object'})
    check(change_null_values(coffee_shop), ['id', 'drink'], [[9, 'Rum and Coke'], [6, 'Rum and Coke'], [7, 'Rum and Coke'], [3, 'St Germain Spritz'], [1, 'Orange Margarita'], [2, 'Orange Margarita']], ordered=False)
