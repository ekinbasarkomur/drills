"""
2879. Display the First Three Rows · Easy · https://leetcode.com/problems/display-the-first-three-rows/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name', 'department', 'salary'], [[3, 'Bob', 'Operations', 48675], [90, 'Alice', 'Sales', 11096], [9, 'Tatiana', 'Engineering', 33805], [60, 'Annabelle', 'InformationTechnology', 37678], [49, 'Jonathan', 'HumanResources', 23793], [43, 'Khaled', 'Administration', 40454]], {'employee_id': 'Int64', 'name': 'object', 'department': 'object', 'salary': 'Int64'})
    check(selectFirstRows(employees), ['employee_id', 'name', 'department', 'salary'], [[3, 'Bob', 'Operations', 48675], [90, 'Alice', 'Sales', 11096], [9, 'Tatiana', 'Engineering', 33805]], ordered=False)
