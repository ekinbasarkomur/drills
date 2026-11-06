"""
197. Rising Temperature · Easy · https://leetcode.com/problems/rising-temperature/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    weather = frame(['id', 'recordDate', 'temperature'], [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]], {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'})
    check(rising_temperature(weather), ['id'], [[2], [4]], ordered=False)
