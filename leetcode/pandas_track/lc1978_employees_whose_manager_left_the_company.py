"""
1978. Employees Whose Manager Left the Company · Easy · https://leetcode.com/problems/employees-whose-manager-left-the-company/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name', 'manager_id', 'salary'], [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241], [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]], {'employee_id': 'Int64', 'name': 'object', 'manager_id': 'Int64', 'salary': 'Int64'})
    check(find_employees(employees), ['employee_id'], [[11]], ordered=True)
