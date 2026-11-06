"""
3188. Find Top Scoring Students II · Hard · https://leetcode.com/problems/find-top-scoring-students-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_top_scoring_students(students: pd.DataFrame, courses: pd.DataFrame, enrollments: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'name', 'major'], [[1, 'Alice', 'Computer Science'], [2, 'Bob', 'Computer Science'], [3, 'Charlie', 'Mathematics'], [4, 'David', 'Mathematics']], {})
    courses = frame(['course_id', 'name', 'credits', 'major', 'mandatory'], [[101, 'Algorithms', 3, 'Computer Science', 'Yes'], [102, 'Data Structures', 3, 'Computer Science', 'Yes'], [103, 'Calculus', 4, 'Mathematics', 'Yes'], [104, 'Linear Algebra', 4, 'Mathematics', 'Yes'], [105, 'Machine Learning', 3, 'Computer Science', 'No'], [106, 'Probability', 3, 'Mathematics', 'No'], [107, 'Operating Systems', 3, 'Computer Science', 'No'], [108, 'Statistics', 3, 'Mathematics', 'No']], {'course_id': 'Int64', 'name': 'string', 'credits': 'Int64', 'major': 'string', 'mandatory': 'string'})
    enrollments = frame(['student_id', 'course_id', 'semester', 'grade', 'GPA'], [[1, 101, 'Fall 2023', 'A', 4.0], [1, 102, 'Spring 2023', 'A', 4.0], [1, 105, 'Spring 2023', 'A', 4.0], [1, 107, 'Fall 2023', 'B', 3.5], [2, 101, 'Fall 2023', 'A', 4.0], [2, 102, 'Spring 2023', 'B', 3.0], [3, 103, 'Fall 2023', 'A', 4.0], [3, 104, 'Spring 2023', 'A', 4.0], [3, 106, 'Spring 2023', 'A', 4.0], [3, 108, 'Fall 2023', 'B', 3.5], [4, 103, 'Fall 2023', 'B', 3.0], [4, 104, 'Spring 2023', 'B', 3.0]], {'student_id': 'Int64', 'course_id': 'Int64', 'semester': 'string', 'grade': 'string', 'GPA': 'float'})
    check(find_top_scoring_students(students, courses, enrollments), ['student_id'], [[1], [3]], ordered=True)
