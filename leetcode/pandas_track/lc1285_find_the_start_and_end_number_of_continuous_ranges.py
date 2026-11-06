"""
1285. Find the Start and End Number of Continuous Ranges · Medium · https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    logs = frame(['log_id'], [[1], [2], [3], [7], [8], [10]], {'log_id': 'Int64'})
    check(find_continuous_ranges(logs), ['start_id', 'end_id'], [[1, 3], [7, 8], [10, 10]], ordered=True)
