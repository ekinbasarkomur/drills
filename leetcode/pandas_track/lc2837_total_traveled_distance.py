"""
2837. Total Traveled Distance · Easy · https://leetcode.com/problems/total-traveled-distance/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'name'], [[17, 'Addison'], [14, 'Ethan'], [4, 'Michael'], [2, 'Avery'], [10, 'Eleanor']], {'user_id': 'Int64', 'name': 'object'})
    rides = frame(['ride_id', 'user_id', 'distance'], [[72, 17, 160], [42, 14, 161], [45, 4, 59], [32, 2, 197], [15, 4, 357], [56, 2, 196], [10, 14, 25]], {'ride_id': 'Int64', 'user_id': 'Int64', 'distance': 'Int64'})
    check(get_total_distance(users, rides), ['user_id', 'name', 'traveled distance'], [[2, 'Avery', 393], [4, 'Michael', 416], [10, 'Eleanor', 0], [14, 'Ethan', 186], [17, 'Addison', 160]], ordered=True)
