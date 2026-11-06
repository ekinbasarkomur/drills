"""
1270. All People Report to the Given Manager · Medium · https://leetcode.com/problems/all-people-report-to-the-given-manager/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'employee_name', 'manager_id'], [[1, 'Boss', 1], [3, 'Alice', 3], [2, 'Bob', 1], [4, 'Daniel', 2], [7, 'Luis', 4], [8, 'John', 3], [9, 'Angela', 8], [77, 'Robert', 1]], {'employee_id': 'Int64', 'employee_name': 'object', 'manager_id': 'Int64'})
    check(find_reporting_people(employees), ['employee_id'], [[2], [77], [4], [7]], ordered=False)
