"""
178. Rank Scores · Medium · https://leetcode.com/problems/rank-scores/
Plan: 30 Days of Pandas · Gün 13 · Data Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    scores = frame(['id', 'score'], [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]], {'id': 'Int64', 'score': 'Float64'})
    check(order_scores(scores), ['score', 'rank'], [[4.0, 1], [4.0, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.5, 4]], ordered=True)
