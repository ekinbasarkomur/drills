"""
2377. Sort the Olympic Table · Easy · https://leetcode.com/problems/sort-the-olympic-table/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    olympic = frame(['country', 'gold_medals', 'silver_medals', 'bronze_medals'], [['China', 10, 10, 20], ['South Sudan', 0, 0, 1], ['USA', 10, 10, 20], ['Israel', 2, 2, 3], ['Egypt', 2, 2, 2]], {'country': 'object', 'gold_medals': 'Int64', 'silver_medals': 'Int64', 'bronze_medals': 'Int64'})
    check(sort_table(olympic), ['country', 'gold_medals', 'silver_medals', 'bronze_medals'], [['China', 10, 10, 20], ['USA', 10, 10, 20], ['Israel', 2, 2, 3], ['Egypt', 2, 2, 2], ['South Sudan', 0, 0, 1]], ordered=False)
