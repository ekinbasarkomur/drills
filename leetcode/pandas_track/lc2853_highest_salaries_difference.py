"""
2853. Highest Salaries Difference · Easy · https://leetcode.com/problems/highest-salaries-difference/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    salaries = frame(['emp_name', 'department', 'salary'], [['Kathy', 'Engineering', 50000], ['Roy', 'Marketing', 30000], ['Charles', 'Engineering', 45000], ['Jack', 'Engineering', 85000], ['Benjamin', 'Marketing', 34000], ['Anthony', 'Marketing', 42000], ['Edward', 'Engineering', 102000], ['Terry', 'Engineering', 44000], ['Evelyn', 'Marketing', 53000], ['Arthur', 'Engineering', 32000]], {'emp_name': 'object', 'department': 'object', 'salary': 'Int64'})
    check(salaries_difference(salaries), ['salary_difference'], [[49000]], ordered=False)
