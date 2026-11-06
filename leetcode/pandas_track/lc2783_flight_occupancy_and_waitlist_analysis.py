"""
2783. Flight Occupancy and Waitlist Analysis · Medium · https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def waitlist_analysis(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    flights = frame(['flight_id', 'capacity'], [[1, 2], [2, 2], [3, 1]], {'flight_id': 'Int64', 'capacity': 'Int64'})
    passengers = frame(['passenger_id', 'flight_id'], [[101, 1], [102, 1], [103, 1], [104, 2], [105, 2], [106, 3], [107, 3]], {'passenger_id': 'Int64', 'flight_id': 'Int64'})
    check(waitlist_analysis(flights, passengers), ['flight_id', 'booked_cnt', 'waitlist_cnt'], [[1, 2, 1], [2, 2, 0], [3, 1, 1]], ordered=True)
