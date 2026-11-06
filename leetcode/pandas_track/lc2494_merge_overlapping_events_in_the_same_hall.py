"""
2494. Merge Overlapping Events in the Same Hall · Hard · https://leetcode.com/problems/merge-overlapping-events-in-the-same-hall/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def merge_events(hall_events: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    hall_events = frame(['hall_id', 'start_day', 'end_day'], [[1, '2023-01-13', '2023-01-14'], [1, '2023-01-14', '2023-01-17'], [1, '2023-01-18', '2023-01-25'], [2, '2022-12-09', '2022-12-23'], [2, '2022-12-13', '2022-12-17'], [3, '2022-12-01', '2023-01-30']], {'hall_id': 'Int64', 'start_day': 'datetime64[ns]', 'end_day': 'datetime64[ns]'})
    check(merge_events(hall_events), ['hall_id', 'start_day', 'end_day'], [[1, '2023-01-13', '2023-01-17'], [1, '2023-01-18', '2023-01-25'], [2, '2022-12-09', '2022-12-23'], [3, '2022-12-01', '2023-01-30']], ordered=False)
