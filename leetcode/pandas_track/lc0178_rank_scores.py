"""
178. Rank Scores · Medium · https://leetcode.com/problems/rank-scores/
Plan: 30 Days of Pandas · Gün 13 · Data Manipulation

Problem: rank the scores from highest to lowest; equal scores share a rank and ranks have no gaps, output score and rank sorted by score descending.
Approach: sort by score descending and let rank(method="dense", ascending=False) number the distinct values; ties get the same rank and the next distinct value gets the next integer.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by="score", ascending=False)
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    return scores[["score", "rank"]]


# ---------------------------------------------------------------- tests


def test_example_1():
    scores = frame(
        ["id", "score"],
        [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]],
        {"id": "Int64", "score": "Float64"},
    )
    check(
        order_scores(scores),
        ["score", "rank"],
        [[4.0, 1], [4.0, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.5, 4]],
        ordered=True,
    )
