"""
2687. Bikes Last Time Used  · Easy · https://leetcode.com/problems/bikes-last-time-used/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    bikes = frame(['ride_id', 'bike_number', 'start_time', 'end_time'], [[1, 'W00576', '2012-03-25 11:30:00', '2012-03-25 12:40:00'], [2, 'W00300', '2012-03-25 10:30:00', '2012-03-25 10:50:00'], [3, 'W00455', '2012-03-26 14:30:00', '2012-03-26 17:40:00'], [4, 'W00455', '2012-03-25 12:30:00', '2012-03-25 13:40:00'], [5, 'W00576', '2012-03-25 08:10:00', '2012-03-25 09:10:00'], [6, 'W00576', '2012-03-28 02:30:00', '2012-03-28 02:50:00']], {'ride_id': 'Int64', 'bike_number': 'object', 'start_time': 'datetime64[ns]', 'end_time': 'datetime64[ns]'})
    check(last_used_time(bikes), ['bike_number', 'end_time'], [['W00576', '2012-03-28 02:50:00'], ['W00455', '2012-03-26 17:40:00'], ['W00300', '2012-03-25 10:50:00']], ordered=True)
