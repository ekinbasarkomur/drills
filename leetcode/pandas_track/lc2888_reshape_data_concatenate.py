"""
2888. Reshape Data: Concatenate · Easy · https://leetcode.com/problems/reshape-data-concatenate/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: stack the two DataFrames vertically (rows of df2 under df1).
Approach: pd.concat([df1, df2]) with the default axis=0 appends the rows; the columns match by name
Time O(n + m), space O(n + m)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2])
    return result


# ---------------------------------------------------------------- tests


def test_example_1():
    df1 = frame(
        ["student_id", "name", "age"],
        [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17]],
        {"student_id": "Int64", "name": "object", "age": "Int64"},
    )
    df2 = frame(
        ["student_id", "name", "age"],
        [[5, "Leo", 7], [6, "Alex", 7]],
        {"student_id": "Int64", "name": "object", "age": "Int64"},
    )
    check(
        concatenateTables(df1, df2),
        ["student_id", "name", "age"],
        [
            [1, "Mason", 8],
            [2, "Ava", 6],
            [3, "Taylor", 15],
            [4, "Georgia", 17],
            [5, "Leo", 7],
            [6, "Alex", 7],
        ],
        ordered=False,
    )
