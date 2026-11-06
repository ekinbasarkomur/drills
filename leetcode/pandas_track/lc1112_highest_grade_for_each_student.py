"""
1112. Highest Grade For Each Student · Medium · https://leetcode.com/problems/highest-grade-for-each-student/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    enrollments = frame(['student_id', 'course_id', 'grade'], [[2, 2, 95], [2, 3, 95], [1, 1, 90], [1, 2, 99], [3, 1, 80], [3, 2, 75], [3, 3, 82]], {'student_id': 'Int64', 'course_id': 'Int64', 'grade': 'Int64'})
    check(highest_grade(enrollments), ['student_id', 'course_id', 'grade'], [[1, 2, 99], [2, 2, 95], [3, 3, 82]], ordered=True)
