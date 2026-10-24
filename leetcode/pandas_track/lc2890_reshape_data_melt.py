"""
2890. Reshape Data: Melt · Easy · https://leetcode.com/problems/reshape-data-melt/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    report = frame(['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], [['Umbrella', 417, 224, 379, 611], ['SleepingBag', 800, 936, 93, 875]], {'product': 'object', 'quarter_1': 'Int64', 'quarter_2': 'Int64', 'quarter_3': 'Int64', 'quarter_4': 'Int64'})
    check(meltTable(report), ['product', 'quarter', 'sales'], [['Umbrella', 'quarter_1', 417], ['SleepingBag', 'quarter_1', 800], ['Umbrella', 'quarter_2', 224], ['SleepingBag', 'quarter_2', 936], ['Umbrella', 'quarter_3', 379], ['SleepingBag', 'quarter_3', 93], ['Umbrella', 'quarter_4', 611], ['SleepingBag', 'quarter_4', 875]], ordered=False)
