"""
2004. The Number of Seniors and Juniors to Join the Company · Hard · https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_seniors_and_juniors(candidates: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    candidates = frame(['employee_id', 'experience', 'salary'], [[1, 'Junior', 10000], [9, 'Junior', 10000], [2, 'Senior', 20000], [11, 'Senior', 20000], [13, 'Senior', 50000], [4, 'Junior', 40000]], {'employee_id': 'Int64', 'experience': 'object', 'salary': 'Int64'})
    check(count_seniors_and_juniors(candidates), ['experience', 'accepted_candidates'], [['Senior', 2], ['Junior', 2]], ordered=False)


def test_example_2():
    candidates = frame(['employee_id', 'experience', 'salary'], [[1, 'Junior', 10000], [9, 'Junior', 10000], [2, 'Senior', 80000], [11, 'Senior', 80000], [13, 'Senior', 80000], [4, 'Junior', 40000]], {'employee_id': 'Int64', 'experience': 'object', 'salary': 'Int64'})
    check(count_seniors_and_juniors(candidates), ['experience', 'accepted_candidates'], [['Senior', 0], ['Junior', 3]], ordered=False)
