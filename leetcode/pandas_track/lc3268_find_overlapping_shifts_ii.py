"""
3268. Find Overlapping Shifts II · Hard · https://leetcode.com/problems/find-overlapping-shifts-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_shift_overlaps(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee_shifts = frame(['employee_id', 'start_time', 'end_time'], [[1, '2023-10-01 09:00:00', '2023-10-01 17:00:00'], [1, '2023-10-01 15:00:00', '2023-10-01 23:00:00'], [1, '2023-10-01 16:00:00', '2023-10-02 00:00:00'], [2, '2023-10-01 09:00:00', '2023-10-01 17:00:00'], [2, '2023-10-01 11:00:00', '2023-10-01 19:00:00'], [3, '2023-10-01 09:00:00', '2023-10-01 17:00:00']], {})
    check(calculate_shift_overlaps(employee_shifts), ['employee_id', 'max_overlapping_shifts', 'total_overlap_duration'], [[1, 3, 600], [2, 2, 360], [3, 1, 0]], ordered=True)
