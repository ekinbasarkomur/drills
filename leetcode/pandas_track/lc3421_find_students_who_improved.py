"""
3421. Find Students Who Improved · Medium · https://leetcode.com/problems/find-students-who-improved/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    scores = frame(['student_id', 'subject', 'score', 'exam_date'], [[101, 'Math', 70, '2023-01-15'], [101, 'Math', 85, '2023-02-15'], [101, 'Physics', 65, '2023-01-15'], [101, 'Physics', 60, '2023-02-15'], [102, 'Math', 80, '2023-01-15'], [102, 'Math', 85, '2023-02-15'], [103, 'Math', 90, '2023-01-15'], [104, 'Physics', 75, '2023-01-15'], [104, 'Physics', 85, '2023-02-15']], {})
    check(find_students_who_improved(scores), ['student_id', 'subject', 'first_score', 'latest_score'], [[101, 'Math', 70, 85], [102, 'Math', 80, 85], [104, 'Physics', 75, 85]], ordered=True)
