"""
1873. Calculate Special Bonus · Easy · https://leetcode.com/problems/calculate-special-bonus/
Plan: 30 Days of Pandas · Gün 6 · String Methods

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name', 'salary'], [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]], {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
    check(calculate_special_bonus(employees), ['employee_id', 'bonus'], [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]], ordered=True)
