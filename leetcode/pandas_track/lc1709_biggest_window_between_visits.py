"""
1709. Biggest Window Between Visits · Medium · https://leetcode.com/problems/biggest-window-between-visits/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_visits = frame(['user_id', 'visit_date'], [['1', '2020-11-28'], ['1', '2020-10-20'], ['1', '2020-12-3'], ['2', '2020-10-5'], ['2', '2020-12-9'], ['3', '2020-11-11']], {'user_id': 'Int64', 'visit_date': 'datetime64[ns]'})
    check(biggest_window(user_visits), ['user_id', 'biggest_window'], [[1, 39], [2, 65], [3, 51]], ordered=True)
