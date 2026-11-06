"""
1731. The Number of Employees Which Report to Each Employee · Easy · https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name', 'reports_to', 'age'], [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]], {'employee_id': 'Int64', 'name': 'object', 'reports_to': 'Int64', 'age': 'Int64'})
    check(count_employees(employees), ['employee_id', 'name', 'reports_count', 'average_age'], [[9, 'Hercy', 2, 39]], ordered=True)


def test_example_2():
    employees = frame(['employee_id', 'name', 'reports_to', 'age'], [[1, 'Michael', None, 45], [2, 'Alice', 1, 38], [3, 'Bob', 1, 42], [4, 'Charlie', 2, 34], [5, 'David', 2, 40], [6, 'Eve', 3, 37], [7, 'Frank', None, 50], [8, 'Grace', None, 48]], {'employee_id': 'Int64', 'name': 'object', 'reports_to': 'Int64', 'age': 'Int64'})
    check(count_employees(employees), ['employee_id', 'name', 'reports_count', 'average_age'], [['-----------', '-------', '-------------', '-----------'], [1, 'Michael', 2, 40], [2, 'Alice', 2, 37], [3, 'Bob', 1, 37]], ordered=True)
