"""
580. Count Student Number in Departments · Medium · https://leetcode.com/problems/count-student-number-in-departments/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    student = frame(['student_id', 'student_name', 'gender', 'dept_id'], [[1, 'Jack', 'M', 1], [2, 'Jane', 'F', 1], [3, 'Mark', 'M', 2]], {'student_id': 'Int64', 'student_name': 'object', 'gender': 'object', 'dept_id': 'Int64'})
    department = frame(['dept_id', 'dept_name'], [[1, 'Engineering'], [2, 'Science'], [3, 'Law']], {'dept_id': 'Int64', 'dept_name': 'object'})
    check(count_students(student, department), ['dept_name', 'student_number'], [['Engineering', 2], ['Science', 1], ['Law', 0]], ordered=True)
