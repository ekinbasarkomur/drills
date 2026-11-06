"""
2314. The First Day of the Maximum Recorded Degree in Each City · Medium · https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    weather = frame(['city_id', 'day', 'degree'], [[1, '2022-01-07', -12], [1, '2022-03-07', 5], [1, '2022-07-07', 24], [2, '2022-08-07', 37], [2, '2022-08-17', 37], [3, '2022-02-07', -7], [3, '2022-12-07', -6]], {'city_id': 'Int64', 'day': 'datetime64[ns]', 'degree': 'Int64'})
    check(find_the_first_day(weather), ['city_id', 'day', 'degree'], [[1, '2022-07-07', 24], [2, '2022-08-07', 37], [3, '2022-12-07', -6]], ordered=True)
