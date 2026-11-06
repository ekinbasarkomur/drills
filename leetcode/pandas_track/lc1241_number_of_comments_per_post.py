"""
1241. Number of Comments per Post · Easy · https://leetcode.com/problems/number-of-comments-per-post/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    submissions = frame(['sub_id', 'parent_id'], [[1, None], [2, None], [1, None], [12, None], [3, 1], [5, 2], [3, 1], [4, 1], [9, 1], [10, 2], [6, 7]], {'sub_id': 'Int64', 'parent_id': 'Int64'})
    check(count_comments(submissions), ['post_id', 'number_of_comments'], [[1, 3], [2, 2], [12, 0]], ordered=True)
