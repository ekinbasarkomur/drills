"""
626. Exchange Seats · Medium · https://leetcode.com/problems/exchange-seats/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    seat = frame(['id', 'student'], [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']], {'id': 'Int64', 'student': 'object'})
    check(exchange_seats(seat), ['id', 'student'], [[1, 'Doris'], [2, 'Abbot'], [3, 'Green'], [4, 'Emerson'], [5, 'Jeames']], ordered=True)
