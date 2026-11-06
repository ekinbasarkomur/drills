"""
3262. Find Overlapping Shifts · Medium · https://leetcode.com/problems/find-overlapping-shifts/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_overlapping_shifts(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee_shifts = frame(['employee_id', 'start_time', 'end_time'], [[1, '08:00:00', '12:00:00'], [1, '11:00:00', '15:00:00'], [1, '14:00:00', '18:00:00'], [2, '09:00:00', '17:00:00'], [2, '16:00:00', '20:00:00'], [3, '10:00:00', '12:00:00'], [3, '13:00:00', '15:00:00'], [3, '16:00:00', '18:00:00'], [4, '08:00:00', '10:00:00'], [4, '09:00:00', '11:00:00']], {})
    check(find_overlapping_shifts(employee_shifts), ['employee_id', 'overlapping_shifts'], [[1, 2], [2, 1], [4, 1]], ordered=True)
