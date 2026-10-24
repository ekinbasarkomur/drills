"""
2883. Drop Missing Data · Easy · https://leetcode.com/problems/drop-missing-data/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: drop the rows whose name is missing.
Approach: dropna(subset=['name']): a row is dropped only if name is NaN/None; missing values in other columns do not count
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])


# ---------------------------------------------------------------- tests


def test_example_1():
    students = frame(
        ["student_id", "name", "age"],
        [[32, "Piper", 5], [217, None, 19], [779, "Georgia", 20], [849, "Willow", 14]],
        {"student_id": "Int64", "name": "object", "age": "Int64"},
    )
    check(
        dropMissingData(students),
        ["student_id", "name", "age"],
        [[32, "Piper", 5], [779, "Georgia", 20], [849, "Willow", 14]],
        ordered=False,
    )
