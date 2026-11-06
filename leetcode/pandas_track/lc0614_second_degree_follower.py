"""
614. Second Degree Follower · Medium · https://leetcode.com/problems/second-degree-follower/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    follow = frame(['followee', 'follower'], [['Alice', 'Bob'], ['Bob', 'Cena'], ['Bob', 'Donald'], ['Donald', 'Edward']], {'followee': 'object', 'follower': 'object'})
    check(second_degree_follower(follow), ['follower', 'num'], [['Bob', 2], ['Donald', 1]], ordered=True)
