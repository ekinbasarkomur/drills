"""
2877. Create a DataFrame from List · Easy · https://leetcode.com/problems/create-a-dataframe-from-list/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from typing import List

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id", "age"])
# ---------------------------------------------------------------- tests

def test_example_1():
    student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]
    check(createDataframe(student_data), ['student_id', 'age'], [[1, 15], [2, 11], [3, 11], [4, 20]], ordered=True)
