"""
2668. Find Latest Salaries · Easy · https://leetcode.com/problems/find-latest-salaries/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    salary = frame(['emp_id', 'firstname', 'lastname', 'salary', 'department_id'], [[1, 'Todd', 'Wilson', 110000, 'D1006'], [1, 'Todd', 'Wilson', 106119, 'D1006'], [2, 'Justin', 'Simon', 128922, 'D1005'], [2, 'Justin', 'Simon', 130000, 'D1005'], [3, 'Kelly', 'Rosario', 42689, 'D1002'], [4, 'Patricia', 'Powell', 162825, 'D1004'], [4, 'Patricia', 'Powell', 170000, 'D1004'], [5, 'Sherry', 'Golden', 44101, 'D1002'], [6, 'Natasha', 'Swanson', 79632, 'D1005'], [6, 'Natasha', 'Swanson', 90000, 'D1005']], {'emp_id': 'Int64', 'firstname': 'object', 'lastname': 'object', 'salary': 'Int64', 'department_id': 'object'})
    check(find_latest_salaries(salary), ['emp_id', 'firstname', 'lastname', 'salary', 'department_id'], [[1, 'Todd', 'Wilson', 110000, 'D1006'], [2, 'Justin', 'Simon', 130000, 'D1005'], [3, 'Kelly', 'Rosario', 42689, 'D1002'], [4, 'Patricia', 'Powell', 170000, 'D1004'], [5, 'Sherry', 'Golden', 44101, 'D1002'], [6, 'Natasha', 'Swanson', 90000, 'D1005']], ordered=True)
