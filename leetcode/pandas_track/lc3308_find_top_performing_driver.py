"""
3308. Find Top Performing Driver · Medium · https://leetcode.com/problems/find-top-performing-driver/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def get_top_performing_drivers(drivers: pd.DataFrame, vehicles: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    drivers = frame(['driver_id', 'name', 'age', 'experience', 'accidents'], [[1, 'Alice', 34, 10, 1], [2, 'Bob', 45, 20, 3], [3, 'Charlie', 28, 5, 0]], {})
    vehicles = frame(['vehicle_id', 'driver_id', 'model', 'fuel_type', 'mileage'], [[100, 1, 'Sedan', 'Gasoline', 20000], [101, 2, 'SUV', 'Electric', 30000], [102, 3, 'Coupe', 'Gasoline', 15000]], {})
    trips = frame(['trip_id', 'vehicle_id', 'distance', 'duration', 'rating'], [[201, 100, 50, 30, 5], [202, 100, 30, 20, 4], [203, 101, 100, 60, 4], [204, 101, 80, 50, 5], [205, 102, 40, 30, 5], [206, 102, 60, 40, 5]], {})
    check(get_top_performing_drivers(drivers, vehicles, trips), ['fuel_type', 'driver_id', 'rating', 'distance'], [['Electric', 2, 4.5, 180], ['Gasoline', 3, 5.0, 100]], ordered=True)
