"""
2881. Create a New Column · Easy · https://leetcode.com/problems/create-a-new-column/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: add a bonus column that is twice the salary.
Approach: assign a new column: employees['bonus'] = employees['salary'] * 2 (vectorised, no loop)
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['name', 'salary'], [['Piper', 4548], ['Grace', 28150], ['Georgia', 1103], ['Willow', 6593], ['Finn', 74576], ['Thomas', 24433]], {'name': 'object', 'salary': 'Int64'})
    check(createBonusColumn(employees), ['name', 'salary', 'bonus'], [['Piper', 4548, 9096], ['Grace', 28150, 56300], ['Georgia', 1103, 2206], ['Willow', 6593, 13186], ['Finn', 74576, 149152], ['Thomas', 24433, 48866]], ordered=False)
