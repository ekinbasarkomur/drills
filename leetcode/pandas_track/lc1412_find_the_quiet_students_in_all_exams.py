"""
1412. Find the Quiet Students in All Exams · Hard · https://leetcode.com/problems/find-the-quiet-students-in-all-exams/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    student = frame(['student_id', 'student_name'], [[1, 'Daniel'], [2, 'Jade'], [3, 'Stella'], [4, 'Jonathan'], [5, 'Will']], {'student_id': 'Int64', 'student_name': 'object'})
    exam = frame(['exam_id', 'student_id', 'score'], [[10, 1, 70], [10, 2, 80], [10, 3, 90], [20, 1, 80], [30, 1, 70], [30, 3, 80], [30, 4, 90], [40, 1, 60], [40, 2, 70], [40, 4, 80]], {'exam_id': 'Int64', 'student_id': 'Int64', 'score': 'Int64'})
    check(find_quiet_students(student, exam), ['student_id', 'student_name'], [[2, 'Jade']], ordered=True)
