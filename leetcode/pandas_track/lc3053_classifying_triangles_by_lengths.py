"""
3053. Classifying Triangles by Lengths · Easy · https://leetcode.com/problems/classifying-triangles-by-lengths/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    triangles = frame(['A', 'B', 'C'], [[20, 20, 23], [20, 20, 20], [20, 21, 22], [13, 14, 30]], {'A': 'Int64', 'B': 'Int64', 'C': 'Int64'})
    check(type_of_triangle(triangles), ['triangle_type'], [['Isosceles'], ['Equilateral'], ['Scalene'], ['Not A Triangle']], ordered=False)
