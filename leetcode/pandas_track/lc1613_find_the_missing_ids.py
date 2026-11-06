"""
1613. Find the Missing IDs · Medium · https://leetcode.com/problems/find-the-missing-ids/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'customer_name'], [[1, 'Alice'], [4, 'Bob'], [5, 'Charlie']], {'customer_id': 'Int64', 'customer_name': 'object'})
    check(find_missing_ids(customers), ['ids'], [[2], [3]], ordered=True)
