"""
2153. The Number of Passengers in Each Bus II · Hard · https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def number_of_passengers(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    buses = frame(['bus_id', 'arrival_time', 'capacity'], [[1, 2, 1], [2, 4, 10], [3, 7, 2]], {'bus_id': 'Int64', 'arrival_time': 'Int64', 'capacity': 'Int64'})
    passengers = frame(['passenger_id', 'arrival_time'], [[11, 1], [12, 1], [13, 5], [14, 6], [15, 7]], {'passenger_id': 'Int64', 'arrival_time': 'Int64'})
    check(number_of_passengers(buses, passengers), ['bus_id', 'passengers_cnt'], [[1, 1], [2, 1], [3, 2]], ordered=True)
