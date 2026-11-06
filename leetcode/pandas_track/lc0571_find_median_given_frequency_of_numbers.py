"""
571. Find Median Given Frequency of Numbers · Hard · https://leetcode.com/problems/find-median-given-frequency-of-numbers/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    numbers = frame(['num', 'frequency'], [[0, 7], [1, 1], [2, 3], [3, 1]], {'num': 'Int64', 'frequency': 'Int64'})
    check(median_frequency(numbers), ['median'], [[0.0]], ordered=False)
