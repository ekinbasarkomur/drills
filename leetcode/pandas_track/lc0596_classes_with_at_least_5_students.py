"""
596. Classes With at Least 5 Students · Easy · https://leetcode.com/problems/classes-with-at-least-5-students/
Plan: 30 Days of Pandas · Gün 22 · Data Aggregation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    courses = frame(['student', 'class'], [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']], {'student': 'object', 'class': 'object'})
    check(find_classes(courses), ['class'], [['Math']], ordered=False)
