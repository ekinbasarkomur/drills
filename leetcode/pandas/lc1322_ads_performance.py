"""
1322. Ads Performance · Easy · https://leetcode.com/problems/ads-performance/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    ads = frame(['ad_id', 'user_id', 'action'], [[1, 1, 'Clicked'], [2, 2, 'Clicked'], [3, 3, 'Viewed'], [5, 5, 'Ignored'], [1, 7, 'Ignored'], [2, 7, 'Viewed'], [3, 5, 'Clicked'], [1, 4, 'Viewed'], [2, 11, 'Viewed'], [1, 2, 'Clicked']], {'ad_id': 'Int64', 'user_id': 'Int64', 'action': 'object'})
    ads_performance(ads)
