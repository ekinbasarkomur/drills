"""
2887. Fill Missing Data · Easy · https://leetcode.com/problems/fill-missing-data/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    products = frame(['name', 'quantity', 'price'], [['Wristwatch', None, 135], ['WirelessEarbuds', None, 821], ['GolfClubs', 779, 9319], ['Printer', 849, 3051]], {'name': 'object', 'quantity': 'Int64', 'price': 'Int64'})
    check(fillMissingValues(products), ['name', 'quantity', 'price'], [['Wristwatch', 0, 135], ['WirelessEarbuds', 0, 821], ['GolfClubs', 779, 9319], ['Printer', 849, 3051]], ordered=False)
