"""
3087. Find Trending Hashtags · Medium · https://leetcode.com/problems/find-trending-hashtags/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tweets = frame(['user_id', 'tweet_id', 'tweet', 'tweet_date'], [[135, 13, 'Enjoying a great start to the day. #HappyDay', '2024-02-01'], [136, 14, 'Another #HappyDay with good ', '2024-02-03'], [137, 15, 'Productivity peaks! #WorkLife', '2024-02-04'], [138, 16, 'Exploring new tech frontiers. #TechLife', '2024-02-04'], [139, 17, "Gratitude for today's moments. #HappyDay", '2024-02-05'], [140, 18, 'Innovation drives us. #TechLife', '2024-02-07'], [141, 19, "Connecting with nature's serenity. #Nature", '2024-02-09']], {'user_id': 'Int64', 'tweet_id': 'Int64', 'tweet_date': 'datetime64[ns]', 'tweet': 'object'})
    check(find_trending_hashtags(tweets), ['hashtag', 'hashtag_count'], [['#HappyDay', 3], ['#TechLife', 2], ['#WorkLife', 1]], ordered=True)
