"""
585. Investments in 2016 · Medium · https://leetcode.com/problems/investments-in-2016/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    insurance = frame(['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon'], [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]], {'pid': 'Int64', 'tiv_2015': 'Float64', 'tiv_2016': 'Float64', 'lat': 'Float64', 'lon': 'Float64'})
    check(find_investments(insurance), ['tiv_2016'], [[45.0]], ordered=False)
