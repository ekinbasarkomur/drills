"""
1853. Convert Date Format · Easy · https://leetcode.com/problems/convert-date-format/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    days = frame(['day'], [['2022-04-12'], ['2021-08-09'], ['2020-06-26']], {'day': 'datetime64[ns]'})
    check(convert_date_format(days), ['day'], [['Tuesday, April 12, 2022'], ['Monday, August 9, 2021'], ['Friday, June 26, 2020']], ordered=False)
