"""
1280. Students and Examinations · Easy · https://leetcode.com/problems/students-and-examinations/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    students = frame(['student_id', 'student_name'], [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']], {'student_id': 'Int64', 'student_name': 'object'})
    subjects = frame(['subject_name'], [['Math'], ['Physics'], ['Programming']], {'subject_name': 'object'})
    examinations = frame(['student_id', 'subject_name'], [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']], {'student_id': 'Int64', 'subject_name': 'object'})
    check(students_and_examinations(students, subjects, examinations), ['student_id', 'student_name', 'subject_name', 'attended_exams'], [[1, 'Alice', 'Math', 3], [1, 'Alice', 'Physics', 2], [1, 'Alice', 'Programming', 1], [2, 'Bob', 'Math', 1], [2, 'Bob', 'Physics', 0], [2, 'Bob', 'Programming', 1], [6, 'Alex', 'Math', 0], [6, 'Alex', 'Physics', 0], [6, 'Alex', 'Programming', 0], [13, 'John', 'Math', 1], [13, 'John', 'Physics', 1], [13, 'John', 'Programming', 1]], ordered=True)
