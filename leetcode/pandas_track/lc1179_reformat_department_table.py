"""
1179. Reformat Department Table · Easy · https://leetcode.com/problems/reformat-department-table/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    department = frame(['id', 'revenue', 'month'], [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']], {'id': 'Int64', 'revenue': 'Int64', 'month': 'object'})
    check(reformat_table(department), ['id', 'Jan_Revenue', 'Feb_Revenue', 'Mar_Revenue', '...', 'Dec_Revenue'], [[1, 8000, 7000, 6000, '...', None], [2, 9000, None, None, '...', None], [3, None, 10000, None, '...', None]], ordered=False)
