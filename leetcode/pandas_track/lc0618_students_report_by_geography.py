"""
618. Students Report By Geography · Hard · https://leetcode.com/problems/students-report-by-geography/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def geography_report(student: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    student = frame(['name', 'continent'], [['Jane', 'America'], ['Pascal', 'Europe'], ['Xi', 'Asia'], ['Jack', 'America']], {'name': 'object', 'continent': 'object'})
    check(geography_report(student), ['America', 'Asia', 'Europe'], [['Jack', 'Xi', 'Pascal'], ['Jane', None, None]], ordered=False)
