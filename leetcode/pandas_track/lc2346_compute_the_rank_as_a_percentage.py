"""
2346. Compute the Rank as a Percentage · Medium · https://leetcode.com/problems/compute-the-rank-as-a-percentage/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'department_id', 'mark'], [[2, 2, 650], [8, 2, 650], [7, 1, 920], [1, 1, 610], [3, 1, 530]], {'student_id': 'Int64', 'department_id': 'Int64', 'mark': 'Int64'})
    check(compute_rating(students), ['student_id', 'department_id', 'percentage'], [[7, 1, 0.0], [1, 1, 50.0], [3, 1, 100.0], [2, 2, 0.0], [8, 2, 0.0]], ordered=False)
