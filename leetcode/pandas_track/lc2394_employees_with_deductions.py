"""
2394. Employees With Deductions · Medium · https://leetcode.com/problems/employees-with-deductions/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def employees_with_deductions(employees: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'needed_hours'], [[1, 20], [2, 12], [3, 2]], {'employee_id': 'Int64', 'needed_hours': 'Int64'})
    logs = frame(['employee_id', 'in_time', 'out_time'], [[1, '2022-10-01 09:00:00', '2022-10-01 17:00:00'], [1, '2022-10-06 09:05:04', '2022-10-06 17:09:03'], [1, '2022-10-12 23:00:00', '2022-10-13 03:00:01'], [2, '2022-10-29 12:00:00', '2022-10-29 23:58:58']], {'employee_id': 'Int64', 'in_time': 'datetime64[ns]', 'out_time': 'datetime64[ns]'})
    check(employees_with_deductions(employees, logs), ['employee_id'], [[2], [3]], ordered=False)
