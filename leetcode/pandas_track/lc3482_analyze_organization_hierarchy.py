"""
3482. Analyze Organization Hierarchy · Hard · https://leetcode.com/problems/analyze-organization-hierarchy/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'employee_name', 'manager_id', 'salary', 'department'], [[1, 'Alice', None, 12000, 'Executive'], [2, 'Bob', 1, 10000, 'Sales'], [3, 'Charlie', 1, 10000, 'Engineering'], [4, 'David', 2, 7500, 'Sales'], [5, 'Eva', 2, 7500, 'Sales'], [6, 'Frank', 3, 9000, 'Engineering'], [7, 'Grace', 3, 8500, 'Engineering'], [8, 'Hank', 4, 6000, 'Sales'], [9, 'Ivy', 6, 7000, 'Engineering'], [10, 'Judy', 6, 7000, 'Engineering']], {})
    check(analyze_organization_hierarchy(employees), ['employee_id', 'employee_name', 'level', 'team_size', 'budget'], [[1, 'Alice', 1, 9, 84500], [3, 'Charlie', 2, 4, 41500], [2, 'Bob', 2, 3, 31000], [6, 'Frank', 3, 2, 23000], [4, 'David', 3, 1, 13500], [7, 'Grace', 3, 0, 8500], [5, 'Eva', 3, 0, 7500], [9, 'Ivy', 4, 0, 7000], [10, 'Judy', 4, 0, 7000], [8, 'Hank', 4, 0, 6000]], ordered=True)
