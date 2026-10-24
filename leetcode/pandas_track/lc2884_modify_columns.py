"""
2884. Modify Columns · Easy · https://leetcode.com/problems/modify-columns/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['name', 'salary'], [['Jack', 19666], ['Piper', 74754], ['Mia', 62509], ['Ulysses', 54866]], {'name': 'object', 'salary': 'Int64'})
    check(modifySalaryColumn(employees), ['name', 'salary'], [['Jack', 39332], ['Piper', 149508], ['Mia', 125018], ['Ulysses', 109732]], ordered=False)
