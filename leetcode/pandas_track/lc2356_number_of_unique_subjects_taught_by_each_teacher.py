"""
2356. Number of Unique Subjects Taught by Each Teacher · Easy · https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
Plan: 30 Days of Pandas · Gün 21 · Data Aggregation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    teacher = frame(['teacher_id', 'subject_id', 'dept_id'], [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]], {'teacher_id': 'Int64', 'subject_id': 'Int64', 'dept_id': 'Int64'})
    check(count_unique_subjects(teacher), ['teacher_id', 'cnt'], [[1, 2], [2, 4]], ordered=False)
