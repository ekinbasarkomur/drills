"""
1715. Count Apples and Oranges · Medium · https://leetcode.com/problems/count-apples-and-oranges/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    boxes = frame(['box_id', 'chest_id', 'apple_count', 'orange_count'], [[2, None, 6, 15], [18, 14, 4, 15], [19, 3, 8, 4], [12, 2, 19, 20], [20, 6, 12, 9], [8, 6, 9, 9], [3, 14, 16, 7]], {'box_id': 'Int64', 'chest_id': 'Int64', 'apple_count': 'Int64', 'orange_count': 'Int64'})
    chests = frame(['chest_id', 'apple_count', 'orange_count'], [[6, 5, 6], [14, 20, 10], [2, 8, 8], [3, 19, 4], [16, 19, 19]], {'chest_id': 'Int64', 'apple_count': 'Int64', 'orange_count': 'Int64'})
    check(count_apples_and_oranges(boxes, chests), ['apple_count', 'orange_count'], [[151, 123]], ordered=False)
