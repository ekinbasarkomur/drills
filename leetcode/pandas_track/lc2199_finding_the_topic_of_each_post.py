"""
2199. Finding the Topic of Each Post · Hard · https://leetcode.com/problems/finding-the-topic-of-each-post/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    keywords = frame(['topic_id', 'word'], [[1, 'handball'], [1, 'football'], [3, 'WAR'], [2, 'Vaccine']], {'topic_id': 'Int64', 'word': 'object'})
    posts = frame(['post_id', 'content'], [[1, 'We call it soccer They call it football hahaha'], [2, 'Americans prefer basketball while Europeans love handball and football'], [3, 'stop the war and play handball'], [4, 'warning I planted some flowers this morning and then got vaccinated']], {'post_id': 'Int64', 'content': 'object'})
    check(find_topic(keywords, posts), ['post_id', 'topic'], [[1, 1], [2, 1], [3, '1,3'], [4, 'Ambiguous!']], ordered=False)
