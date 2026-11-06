"""
584. Find Customer Referee · Easy · https://leetcode.com/problems/find-customer-referee/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customer = frame(['id', 'name', 'referee_id'], [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]], {'id': 'Int64', 'name': 'object', 'referee_id': 'Int64'})
    check(find_customer_referee(customer), ['name'], [['Will'], ['Jane'], ['Bill'], ['Zack']], ordered=False)
