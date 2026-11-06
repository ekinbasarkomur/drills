"""
2112. The Airport With the Most Traffic · Medium · https://leetcode.com/problems/the-airport-with-the-most-traffic/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    flights = frame(['departure_airport', 'arrival_airport', 'flights_count'], [[1, 2, 4], [2, 1, 5], [2, 4, 5]], {'departure_airport': 'Int64', 'arrival_airport': 'Int64', 'flights_count': 'Int64'})
    check(airport_with_most_traffic(flights), ['airport_id'], [[2]], ordered=False)


def test_example_2():
    flights = frame(['departure_airport', 'arrival_airport', 'flights_count'], [[1, 2, 4], [2, 1, 5], [3, 4, 5], [4, 3, 4], [5, 6, 7]], {'departure_airport': 'Int64', 'arrival_airport': 'Int64', 'flights_count': 'Int64'})
    check(airport_with_most_traffic(flights), ['airport_id'], [[1], [2], [3], [4]], ordered=False)
