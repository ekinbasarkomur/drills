"""
2308. Arrange Table by Gender · Medium · https://leetcode.com/problems/arrange-table-by-gender/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    genders = frame(['user_id', 'gender'], [[4, 'male'], [7, 'female'], [2, 'other'], [5, 'male'], [3, 'female'], [8, 'male'], [6, 'other'], [1, 'other'], [9, 'female']], {'user_id': 'Int64', 'gender': 'object'})
    check(arrange_table(genders), ['user_id', 'gender'], [[3, 'female'], [1, 'other'], [4, 'male'], [7, 'female'], [2, 'other'], [5, 'male'], [9, 'female'], [6, 'other'], [8, 'male']], ordered=False)
