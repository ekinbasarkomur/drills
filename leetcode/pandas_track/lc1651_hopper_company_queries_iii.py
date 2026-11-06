"""
1651. Hopper Company Queries III · Hard · https://leetcode.com/problems/hopper-company-queries-iii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    drivers = frame(['driver_id', 'join_date'], [[10, '2019-12-10'], [8, '2020-1-13'], [5, '2020-2-16'], [7, '2020-3-8'], [4, '2020-5-17'], [1, '2020-10-24'], [6, '2021-1-5']], {'driver_id': 'Int64', 'join_date': 'datetime64[ns]'})
    rides = frame(['ride_id', 'user_id', 'requested_at'], [[6, 75, '2019-12-9'], [1, 54, '2020-2-9'], [10, 63, '2020-3-4'], [19, 39, '2020-4-6'], [3, 41, '2020-6-3'], [13, 52, '2020-6-22'], [7, 69, '2020-7-16'], [17, 70, '2020-8-25'], [20, 81, '2020-11-2'], [5, 57, '2020-11-9'], [2, 42, '2020-12-9'], [11, 68, '2021-1-11'], [15, 32, '2021-1-17'], [12, 11, '2021-1-19'], [14, 18, '2021-1-27']], {'ride_id': 'Int64', 'user_id': 'Int64', 'requested_at': 'datetime64[ns]'})
    accepted_rides = frame(['ride_id', 'driver_id', 'ride_distance', 'ride_duration'], [[10, 10, 63, 38], [13, 10, 73, 96], [7, 8, 100, 28], [17, 7, 119, 68], [20, 1, 121, 92], [5, 7, 42, 101], [2, 4, 6, 38], [11, 8, 37, 43], [15, 8, 108, 82], [12, 8, 38, 34], [14, 1, 90, 74]], {'ride_id': 'Int64', 'driver_id': 'Int64', 'ride_distance': 'Int64', 'ride_duration': 'Int64'})
    check(hopper_company_queries(drivers, rides, accepted_rides), ['month', 'average_ride_distance', 'average_ride_duration'], [[1, 21.0, 12.67], [2, 21.0, 12.67], [3, 21.0, 12.67], [4, 24.33, 32.0], [5, 57.67, 41.33], [6, 97.33, 64.0], [7, 73.0, 32.0], [8, 39.67, 22.67], [9, 54.33, 64.33], [10, 56.33, 77.0]], ordered=True)
