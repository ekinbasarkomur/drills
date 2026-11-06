"""
2010. The Number of Seniors and Juniors to Join the Company II · Hard · https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def number_of_joiners(candidates: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    candidates = frame(['employee_id', 'experience', 'salary'], [[1, 'Junior', 10000], [9, 'Junior', 15000], [2, 'Senior', 20000], [11, 'Senior', 16000], [13, 'Senior', 50000], [4, 'Junior', 40000]], {'employee_id': 'Int64', 'experience': 'object', 'salary': 'Int64'})
    check(number_of_joiners(candidates), ['employee_id'], [[11], [2], [1], [9]], ordered=False)


def test_example_2():
    candidates = frame(['employee_id', 'experience', 'salary'], [[1, 'Junior', 25000], [9, 'Junior', 10000], [2, 'Senior', 85000], [11, 'Senior', 80000], [13, 'Senior', 90000], [4, 'Junior', 30000]], {'employee_id': 'Int64', 'experience': 'object', 'salary': 'Int64'})
    check(number_of_joiners(candidates), ['employee_id'], [[9], [1], [4]], ordered=False)
