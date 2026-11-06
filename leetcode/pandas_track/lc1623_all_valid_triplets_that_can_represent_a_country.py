"""
1623. All Valid Triplets That Can Represent a Country · Easy · https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    school_a = frame(['student_id', 'student_name'], [[1, 'Alice'], [2, 'Bob']], {'student_id': 'Int64', 'student_name': 'object'})
    school_b = frame(['student_id', 'student_name'], [[3, 'Tom']], {'student_id': 'Int64', 'student_name': 'object'})
    school_c = frame(['student_id', 'student_name'], [[3, 'Tom'], [2, 'Jerry'], [10, 'Alice']], {'student_id': 'Int64', 'student_name': 'object'})
    check(find_valid_triplets(school_a, school_b, school_c), ['member_A', 'member_B', 'member_C'], [['Alice', 'Tom', 'Jerry'], ['Bob', 'Tom', 'Alice']], ordered=False)
