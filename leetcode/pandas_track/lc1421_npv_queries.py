"""
1421. NPV Queries · Easy · https://leetcode.com/problems/npv-queries/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    npv = frame(['id', 'year', 'npv'], [[1, 2018, 100], [7, 2020, 30], [13, 2019, 40], [1, 2019, 113], [2, 2008, 121], [3, 2009, 21], [11, 2020, 99], [7, 2019, 0]], {'id': 'Int64', 'year': 'Int64', 'npv': 'Int64'})
    queries = frame(['id', 'year'], [[1, 2019], [2, 2008], [3, 2009], [7, 2018], [7, 2019], [7, 2020], [13, 2019]], {'id': 'Int64', 'year': 'Int64'})
    check(npv_queries(npv, queries), ['id', 'year', 'npv'], [[1, 2019, 113], [2, 2008, 121], [3, 2009, 12], [7, 2018, 0], [7, 2019, 0], [7, 2020, 30], [13, 2019, 40]], ordered=False)
