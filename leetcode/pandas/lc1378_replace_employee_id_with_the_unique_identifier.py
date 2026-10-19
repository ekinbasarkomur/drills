"""
1378. Replace Employee ID With The Unique Identifier · Easy · https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['id', 'name'], [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']], {'id': 'int64', 'name': 'object'})
    employee_uni = frame(['id', 'unique_id'], [[3, 1], [11, 2], [90, 3]], {'id': 'int64', 'unique_id': 'int64'})
    check(replace_employee_id(employees, employee_uni), ['unique_id', 'name'], [[None, 'Alice'], [None, 'Bob'], [2, 'Meir'], [3, 'Winston'], [1, 'Jonathan']], ordered=False)
