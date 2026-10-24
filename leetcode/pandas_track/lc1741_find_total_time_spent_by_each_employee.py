"""
1741. Find Total Time Spent by Each Employee · Easy · https://leetcode.com/problems/find-total-time-spent-by-each-employee/
Plan: 30 Days of Pandas · Gün 19 · Data Aggregation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['emp_id', 'event_day', 'in_time', 'out_time'], [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']], {'emp_id': 'Int64', 'event_day': 'datetime64[ns]', 'in_time': 'Int64', 'out_time': 'Int64'})
    check(total_time(employees), ['day', 'emp_id', 'total_time'], [['2020-11-28', 1, 173], ['2020-11-28', 2, 30], ['2020-12-03', 1, 41], ['2020-12-09', 2, 27]], ordered=False)
