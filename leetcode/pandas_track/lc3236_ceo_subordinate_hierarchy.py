"""
3236. CEO Subordinate Hierarchy · Hard · https://leetcode.com/problems/ceo-subordinate-hierarchy/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_subordinates(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'employee_name', 'manager_id', 'salary'], [[1, 'Alice', None, 150000], [2, 'Bob', 1, 120000], [3, 'Charlie', 1, 110000], [4, 'David', 2, 105000], [5, 'Eve', 2, 100000], [6, 'Frank', 3, 95000], [7, 'Grace', 3, 98000], [8, 'Helen', 5, 90000]], {})
    check(find_subordinates(employees), ['subordinate_id', 'subordinate_name', 'hierarchy_level', 'salary_difference'], [[2, 'Bob', 1, -30000], [3, 'Charlie', 1, -40000], [4, 'David', 2, -45000], [5, 'Eve', 2, -50000], [6, 'Frank', 2, -55000], [7, 'Grace', 2, -52000], [8, 'Helen', 3, -60000]], ordered=True)
