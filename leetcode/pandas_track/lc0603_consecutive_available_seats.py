"""
603. Consecutive Available Seats · Easy · https://leetcode.com/problems/consecutive-available-seats/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    cinema = frame(['seat_id', 'free'], [[1, 1], [2, 0], [3, 1], [4, 1], [5, 1]], {'seat_id': 'Int64', 'free': 'int'})
    check(consecutive_available_seats(cinema), ['seat_id'], [[3], [4], [5]], ordered=True)
