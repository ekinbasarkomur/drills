"""
3156. Employee Task Duration and Concurrent Tasks · Hard · https://leetcode.com/problems/employee-task-duration-and-concurrent-tasks/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_total_duration(tasks: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tasks = frame(['task_id', 'employee_id', 'start_time', 'end_time'], [[1, 1001, '2023-05-01 08:00:00', '2023-05-01 09:00:00'], [2, 1001, '2023-05-01 08:30:00', '2023-05-01 10:30:00'], [3, 1001, '2023-05-01 11:00:00', '2023-05-01 12:00:00'], [7, 1001, '2023-05-01 13:00:00', '2023-05-01 15:30:00'], [4, 1002, '2023-05-01 09:00:00', '2023-05-01 10:00:00'], [5, 1002, '2023-05-01 09:30:00', '2023-05-01 11:30:00'], [6, 1003, '2023-05-01 14:00:00', '2023-05-01 16:00:00']], {})
    check(find_total_duration(tasks), ['employee_id', 'total_task_hours', 'max_concurrent_tasks'], [[1001, 6, 2], [1002, 2, 2], [1003, 2, 1]], ordered=True)
