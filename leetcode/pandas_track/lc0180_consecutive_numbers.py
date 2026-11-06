"""
180. Consecutive Numbers · Medium · https://leetcode.com/problems/consecutive-numbers/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    logs = frame(['id', 'num'], [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]], {'id': 'Int64', 'num': 'Int64'})
    check(consecutive_numbers(logs), ['ConsecutiveNums'], [[1]], ordered=False)
