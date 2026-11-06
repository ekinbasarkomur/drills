"""
1990. Count the Number of Experiments · Medium · https://leetcode.com/problems/count-the-number-of-experiments/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    experiments = frame(['experiment_id', 'platform', 'experiment_name'], [[4, 'IOS', 'Programming'], [13, 'IOS', 'Sports'], [14, 'Android', 'Reading'], [8, 'Web', 'Reading'], [12, 'Web', 'Reading'], [18, 'Web', 'Programming']], {'experiment_id': 'Int64', 'platform': 'object', 'experiment_name': 'object'})
    check(count_experiments(experiments), ['platform', 'experiment_name', 'num_experiments'], [['Android', 'Reading', 1], ['Android', 'Sports', 0], ['Android', 'Programming', 0], ['IOS', 'Reading', 0], ['IOS', 'Sports', 1], ['IOS', 'Programming', 1], ['Web', 'Reading', 2], ['Web', 'Sports', 0], ['Web', 'Programming', 1]], ordered=False)
