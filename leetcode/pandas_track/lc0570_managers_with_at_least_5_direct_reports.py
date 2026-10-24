"""
570. Managers with at Least 5 Direct Reports · Medium · https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
Plan: 30 Days of Pandas · Gün 29 · Data Integration

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employee = frame(['id', 'name', 'department', 'managerId'], [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]], {'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'})
    check(find_managers(employee), ['name'], [['John']], ordered=False)
