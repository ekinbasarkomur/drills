"""
2142. The Number of Passengers in Each Bus I · Medium · https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    buses = frame(['bus_id', 'arrival_time'], [[1, 2], [2, 4], [3, 7]], {'bus_id': 'Int64', 'arrival_time': 'Int64'})
    passengers = frame(['passenger_id', 'arrival_time'], [[11, 1], [12, 5], [13, 6], [14, 7]], {'passenger_id': 'Int64', 'arrival_time': 'Int64'})
    check(count_passengers_in_bus(buses, passengers), ['bus_id', 'passengers_cnt'], [[1, 1], [2, 0], [3, 3]], ordered=True)
