"""
3057. Employees Project Allocation · Hard · https://leetcode.com/problems/employees-project-allocation/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def employees_with_above_avg_workload(project: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    project = frame(['project_id', 'employee_id', 'workload'], [[1, 1, 45], [1, 2, 90], [2, 3, 12], [2, 4, 68]], {'project_id': 'Int64', 'employee_id': 'Int64', 'workload': 'Int64'})
    employees = frame(['employee_id', 'name', 'team'], [[1, 'Khaled', 'A'], [2, 'Ali', 'B'], [3, 'John', 'B'], [4, 'Doe', 'A']], {'employee_id': 'Int64', 'name': 'object', 'team': 'object'})
    check(employees_with_above_avg_workload(project, employees), ['employee_id', 'project_id', 'employee_name', 'project_workload'], [[2, 1, 'Ali', 90], [4, 2, 'Doe', 68]], ordered=True)
