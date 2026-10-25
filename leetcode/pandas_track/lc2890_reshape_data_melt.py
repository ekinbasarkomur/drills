"""
2890. Reshape Data: Melt · Easy · https://leetcode.com/problems/reshape-data-melt/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: turn the wide table into a long one: one row per (product, quarter) with its sales.
Approach: melt keeps product as the id column, turns the quarter_1..4 column names into the quarter column and their values into sales
Time O(n·k), space O(n·k)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars = ['product'],
        value_vars =['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name = 'quarter',
        value_name = 'sales')
# ---------------------------------------------------------------- tests

def test_example_1():
    report = frame(['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], [['Umbrella', 417, 224, 379, 611], ['SleepingBag', 800, 936, 93, 875]], {'product': 'object', 'quarter_1': 'Int64', 'quarter_2': 'Int64', 'quarter_3': 'Int64', 'quarter_4': 'Int64'})
    check(meltTable(report), ['product', 'quarter', 'sales'], [['Umbrella', 'quarter_1', 417], ['SleepingBag', 'quarter_1', 800], ['Umbrella', 'quarter_2', 224], ['SleepingBag', 'quarter_2', 936], ['Umbrella', 'quarter_3', 379], ['SleepingBag', 'quarter_3', 93], ['Umbrella', 'quarter_4', 611], ['SleepingBag', 'quarter_4', 875]], ordered=False)
