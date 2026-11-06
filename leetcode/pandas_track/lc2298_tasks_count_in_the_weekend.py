"""
2298. Tasks Count in the Weekend · Medium · https://leetcode.com/problems/tasks-count-in-the-weekend/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tasks = frame(['task_id', 'assignee_id', 'submit_date'], [[1, 1, '2022-06-13'], [2, 6, '2022-06-14'], [3, 6, '2022-06-15'], [4, 3, '2022-06-18'], [5, 5, '2022-06-19'], [6, 7, '2022-06-19']], {'task_id': 'Int64', 'assignee_id': 'Int64', 'submit_date': 'datetime64[ns]'})
    check(count_tasks(tasks), ['weekend_cnt', 'working_cnt'], [[3, 3]], ordered=False)
