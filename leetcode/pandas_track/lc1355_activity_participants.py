"""
1355. Activity Participants · Medium · https://leetcode.com/problems/activity-participants/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friends = frame(['id', 'name', 'activity'], [[1, 'Jonathan D.', 'Eating'], [2, 'Jade W.', 'Singing'], [3, 'Victor J.', 'Singing'], [4, 'Elvis Q.', 'Eating'], [5, 'Daniel A.', 'Eating'], [6, 'Bob B.', 'Horse Riding']], {'id': 'Int64', 'name': 'object', 'activity': 'object'})
    activities = frame(['id', 'name'], [[1, 'Eating'], [2, 'Singing'], [3, 'Horse Riding']], {'id': 'Int64', 'name': 'object'})
    check(activity_participants(friends, activities), ['activity'], [['Singing']], ordered=False)
