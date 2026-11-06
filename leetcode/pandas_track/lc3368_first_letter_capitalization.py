"""
3368. First Letter Capitalization · Hard · https://leetcode.com/problems/first-letter-capitalization/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_content = frame(['content_id', 'content_text'], [[1, 'hello world of SQL'], [2, 'the QUICK brown fox'], [3, 'data science AND machine learning'], [4, 'TOP rated programming BOOKS']], {})
    check(process_text(user_content), ['content_id', 'original_text', 'converted_text'], [[1, 'hello world of SQL', 'Hello World Of Sql'], [2, 'the QUICK brown fox', 'The Quick Brown Fox'], [3, 'data science AND machine learning', 'Data Science And Machine Learning'], [4, 'TOP rated programming BOOKS', 'Top Rated Programming Books']], ordered=False)
