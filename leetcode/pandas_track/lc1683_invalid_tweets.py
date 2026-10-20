"""
1683. Invalid Tweets · Easy · https://leetcode.com/problems/invalid-tweets/
Plan: 30 Days of Pandas · Gün 5 · String Methods

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tweets = frame(['tweet_id', 'content'], [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']], {'tweet_id': 'Int64', 'content': 'object'})
    check(invalid_tweets(tweets), ['tweet_id'], [[2]], ordered=False)
