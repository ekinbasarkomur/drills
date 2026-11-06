"""
1341. Movie Rating · Medium · https://leetcode.com/problems/movie-rating/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    movies = frame(['movie_id', 'title'], [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']], {'movie_id': 'Int64', 'title': 'object'})
    users = frame(['user_id', 'name'], [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']], {'user_id': 'Int64', 'name': 'object'})
    movie_rating_df = frame(['movie_id', 'user_id', 'rating', 'created_at'], [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']], {'movie_id': 'Int64', 'user_id': 'Int64', 'rating': 'Int64', 'created_at': 'datetime64[ns]'})
    check(movie_rating(movies, users, movie_rating_df), ['results'], [['Daniel'], ['Frozen 2']], ordered=False)
