"""
1393. Capital Gain/Loss · Medium · https://leetcode.com/problems/capital-gainloss/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    stocks = frame(['stock_name', 'operation', 'operation_day', 'price'], [['Leetcode', 'Buy', 1, 1000], ['Corona Masks', 'Buy', 2, 10], ['Leetcode', 'Sell', 5, 9000], ['Handbags', 'Buy', 17, 30000], ['Corona Masks', 'Sell', 3, 1010], ['Corona Masks', 'Buy', 4, 1000], ['Corona Masks', 'Sell', 5, 500], ['Corona Masks', 'Buy', 6, 1000], ['Handbags', 'Sell', 29, 7000], ['Corona Masks', 'Sell', 10, 10000]], {'stock_name': 'object', 'operation': 'object', 'operation_day': 'Int64', 'price': 'Int64'})
    check(capital_gainloss(stocks), ['stock_name', 'capital_gain_loss'], [['Corona Masks', 9500], ['Leetcode', 8000], ['Handbags', -23000]], ordered=False)
