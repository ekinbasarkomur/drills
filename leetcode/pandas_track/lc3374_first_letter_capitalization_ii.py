"""
3374. First Letter Capitalization II · Hard · https://leetcode.com/problems/first-letter-capitalization-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_content = frame(['content_id', 'content_text'], [[1, 'hello world of SQL'], [2, 'the QUICK-brown fox'], [3, 'modern-day DATA science'], [4, 'web-based FRONT-end development']], {})
    check(capitalize_content(user_content), ['content_id', 'original_text', 'converted_text'], [[1, 'hello world of SQL', 'Hello World Of Sql'], [2, 'the QUICK-brown fox', 'The Quick-Brown Fox'], [3, 'modern-day DATA science', 'Modern-Day Data Science'], [4, 'web-based FRONT-end development', 'Web-Based Front-End Development']], ordered=False)
