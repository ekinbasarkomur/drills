"""
1767. Find the Subtasks That Did Not Execute · Hard · https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tasks = frame(['task_id', 'subtasks_count'], [[1, 3], [2, 2], [3, 4]], {'task_id': 'Int64', 'subtasks_count': 'Int64'})
    executed = frame(['task_id', 'subtask_id'], [[1, 2], [3, 1], [3, 2], [3, 3], [3, 4]], {'task_id': 'Int64', 'subtask_id': 'Int64'})
    check(find_subtasks(tasks, executed), ['task_id', 'subtask_id'], [[1, 1], [1, 3], [2, 1], [2, 2]], ordered=False)
