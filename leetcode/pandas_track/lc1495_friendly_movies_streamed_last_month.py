"""
1495. Friendly Movies Streamed Last Month · Easy · https://leetcode.com/problems/friendly-movies-streamed-last-month/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tv_program = frame(['program_date', 'content_id', 'channel'], [['2020-06-10 08:00', 1, 'LC-Channel'], ['2020-05-11 12:00', 2, 'LC-Channel'], ['2020-05-12 12:00', 3, 'LC-Channel'], ['2020-05-13 14:00', 4, 'Disney Ch'], ['2020-06-18 14:00', 4, 'Disney Ch'], ['2020-07-15 16:00', 5, 'Disney Ch']], {'program_date': 'datetime64[ns]', 'content_id': 'Int64', 'channel': 'object'})
    content = frame(['content_id', 'title', 'Kids_content', 'content_type'], [[1, 'Leetcode Movie', 'N', 'Movies'], [2, 'Alg. for Kids', 'Y', 'Series'], [3, 'Database Sols', 'N', 'Series'], [4, 'Aladdin', 'Y', 'Movies'], [5, 'Cinderella', 'Y', 'Movies']], {'content_id': 'object', 'title': 'object', 'Kids_content': 'object', 'content_type': 'object'})
    check(friendly_movies(tv_program, content), ['title'], [['Aladdin']], ordered=False)
