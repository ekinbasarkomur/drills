"""
3103. Find Trending Hashtags II  · Hard · https://leetcode.com/problems/find-trending-hashtags-ii/
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
    tweets = frame(['user_id', 'tweet_id', 'tweet', 'tweet_date'], [[135, 13, 'Enjoying a great start to the day. #HappyDay #MorningVibes', '2024-02-01'], [136, 14, 'Another #HappyDay with good vibes! #FeelGood', '2024-02-03'], [137, 15, 'Productivity peaks! #WorkLife #ProductiveDay', '2024-02-04'], [138, 16, 'Exploring new tech frontiers. #TechLife #Innovation', '2024-02-04'], [139, 17, "Gratitude for today's moments. #HappyDay #Thankful", '2024-02-05'], [140, 18, 'Innovation drives us. #TechLife #FutureTech', '2024-02-07'], [141, 19, "Connecting with nature's serenity. #Nature #Peaceful", '2024-02-09']], {'user_id': 'Int64', 'tweet_id': 'Int64', 'tweet_date': 'datetime64[ns]', 'tweet': 'object'})
    check(find_trending_hashtags(tweets), ['hashtag', 'count'], [['#HappyDay', 3], ['#TechLife', 2], ['#WorkLife', 1]], ordered=True)
