"""
2026. Low-Quality Problems · Easy · https://leetcode.com/problems/low-quality-problems/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    problems = frame(['problem_id', 'likes', 'dislikes'], [[6, 1290, 425], [11, 2677, 8659], [1, 4446, 2760], [7, 8569, 6086], [13, 2050, 4164], [10, 9002, 7446]], {'problem_id': 'Int64', 'likes': 'Int64', 'dislikes': 'Int64'})
    check(low_quality_problems(problems), ['problem_id'], [[7], [10], [11], [13]], ordered=True)
