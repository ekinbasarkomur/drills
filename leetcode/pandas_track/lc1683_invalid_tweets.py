"""
1683. Invalid Tweets · Easy · https://leetcode.com/problems/invalid-tweets/
Plan: 30 Days of Pandas · Gün 5 · String Methods

Problem: the ids of tweets whose content is longer than 15 characters.
Approach: a boolean mask from the string length of each content (.str.len() > 15),
          then .loc picks those rows and only the tweet_id column.
Time O(n), space O(n)
"""

# ---------------------------------------------------------------- solution
import pandas as pd
from _pd import check, frame  # isort: skip


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweets = tweets.loc[tweets["content"].str.len() > 15, ["tweet_id"]]

    return tweets


# ---------------------------------------------------------------- tests


def test_example_1():
    tweets = frame(
        ["tweet_id", "content"],
        [[1, "Let us Code"], [2, "More than fifteen chars are here!"]],
        {"tweet_id": "Int64", "content": "object"},
    )
    check(invalid_tweets(tweets), ["tweet_id"], [[2]], ordered=False)
