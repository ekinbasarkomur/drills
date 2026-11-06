"""
1789. Primary Department for Each Employee · Easy · https://leetcode.com/problems/primary-department-for-each-employee/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['employee_id', 'department_id', 'primary_flag'], [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']], {'employee_id': 'Int64', 'department_id': 'Int64', 'primary_flag': 'object'})
    check(find_primary_department(employee), ['employee_id', 'department_id'], [[1, 1], [2, 1], [3, 3], [4, 3]], ordered=False)
