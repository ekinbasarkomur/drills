"""
2886. Change Data Type · Easy · https://leetcode.com/problems/change-data-type/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: convert the grade column from float to int.
Approach: astype(int) converts the whole column to integers (it truncates decimals and fails on NaN); assign it back to the same column
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students


# ---------------------------------------------------------------- tests


def test_example_1():
    students = frame(
        ["student_id", "name", "age", "grade"],
        [[1, "Ava", 6, 73.0], [2, "Kate", 15, 87.0]],
        {"student_id": "Int64", "name": "object", "age": "Int64", "grade": "Float64"},
    )
    check(
        changeDatatype(students),
        ["student_id", "name", "age", "grade"],
        [[1, "Ava", 6, 73], [2, "Kate", 15, 87]],
        ordered=False,
    )
