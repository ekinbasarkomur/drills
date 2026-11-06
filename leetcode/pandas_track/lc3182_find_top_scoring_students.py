"""
3182. Find Top Scoring Students · Medium · https://leetcode.com/problems/find-top-scoring-students/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    enrollments = frame(['student_id', 'course_id', 'semester', 'grade'], [[1, 101, 'Fall 2023', 'A'], [1, 102, 'Fall 2023', 'A'], [2, 101, 'Fall 2023', 'B'], [2, 102, 'Fall 2023', 'A'], [3, 103, 'Fall 2023', 'A'], [3, 104, 'Fall 2023', 'A'], [4, 103, 'Fall 2023', 'A'], [4, 104, 'Fall 2023', 'B']], {})
    students = frame(['student_id', 'name', 'major'], [[1, 'Alice', 'Computer Science'], [2, 'Bob', 'Computer Science'], [3, 'Charlie', 'Mathematics'], [4, 'David', 'Mathematics']], {})
    courses = frame(['course_id', 'name', 'credits', 'major'], [[101, 'Algorithms', 3, 'Computer Science'], [102, 'Data Structures', 3, 'Computer Science'], [103, 'Calculus', 4, 'Mathematics'], [104, 'Linear Algebra', 4, 'Mathematics']], {})
    check(find_top_scoring_students(enrollments, students, courses), ['student_id'], [[1], [3]], ordered=True)
