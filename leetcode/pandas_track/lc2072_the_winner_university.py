"""
2072. The Winner University · Easy · https://leetcode.com/problems/the-winner-university/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    new_york = frame(['student_id', 'score'], [[1, 90], [2, 87]], {'student_id': 'Int64', 'score': 'Int64'})
    california = frame(['student_id', 'score'], [[2, 89], [3, 88]], {'student_id': 'Int64', 'score': 'Int64'})
    check(find_winner(new_york, california), ['winner'], [['New York University']], ordered=False)


def test_example_2():
    new_york = frame(['student_id', 'score'], [[1, 89], [2, 88]], {'student_id': 'Int64', 'score': 'Int64'})
    california = frame(['student_id', 'score'], [[2, 90], [3, 87]], {'student_id': 'Int64', 'score': 'Int64'})
    check(find_winner(new_york, california), ['winner'], [['California University']], ordered=False)


def test_example_3():
    new_york = frame(['student_id', 'score'], [[1, 89], [2, 90]], {'student_id': 'Int64', 'score': 'Int64'})
    california = frame(['student_id', 'score'], [[2, 87], [3, 99]], {'student_id': 'Int64', 'score': 'Int64'})
    check(find_winner(new_york, california), ['winner'], [['No Winner']], ordered=False)
