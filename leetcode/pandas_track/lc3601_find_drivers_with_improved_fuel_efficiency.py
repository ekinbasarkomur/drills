"""
3601. Find Drivers with Improved Fuel Efficiency · Medium · https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    drivers = frame(['driver_id', 'driver_name'], [[1, 'Alice Johnson'], [2, 'Bob Smith'], [3, 'Carol Davis'], [4, 'David Wilson'], [5, 'Emma Brown']], {})
    trips = frame(['trip_id', 'driver_id', 'trip_date', 'distance_km', 'fuel_consumed'], [[1, 1, '2023-02-15', 120.5, 10.2], [2, 1, '2023-03-20', 200.0, 16.5], [3, 1, '2023-08-10', 150.0, 11.0], [4, 1, '2023-09-25', 180.0, 12.5], [5, 2, '2023-01-10', 100.0, 9.0], [6, 2, '2023-04-15', 250.0, 22.0], [7, 2, '2023-10-05', 200.0, 15.0], [8, 3, '2023-03-12', 80.0, 8.5], [9, 3, '2023-05-18', 90.0, 9.2], [10, 4, '2023-07-22', 160.0, 12.8], [11, 4, '2023-11-30', 140.0, 11.0], [12, 5, '2023-02-28', 110.0, 11.5]], {})
    check(find_improved_efficiency_drivers(drivers, trips), ['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement'], [[2, 'Bob Smith', 11.24, 13.33, 2.1], [1, 'Alice Johnson', 11.97, 14.02, 2.05]], ordered=True)
