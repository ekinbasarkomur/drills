"""
2238. Number of Times a Driver Was a Passenger · Medium · https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    rides = frame(['ride_id', 'driver_id', 'passenger_id'], [[1, 7, 1], [2, 7, 2], [3, 11, 1], [4, 11, 7], [5, 11, 7], [6, 11, 3]], {'ride_id': 'Int64', 'driver_id': 'Int64', 'passenger_id': 'Int64'})
    check(driver_passenger(rides), ['driver_id', 'cnt'], [[7, 2], [11, 0]], ordered=False)
