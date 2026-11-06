"""
620. Not Boring Movies · Easy · https://leetcode.com/problems/not-boring-movies/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    cinema = frame(['id', 'movie', 'description', 'rating'], [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]], {'id': 'Int64', 'movie': 'object', 'description': 'object', 'rating': 'Float64'})
    check(not_boring_movies(cinema), ['id', 'movie', 'description', 'rating'], [[5, 'House card', 'Interesting', 9.1], [1, 'War', 'great 3D', 8.9]], ordered=True)
