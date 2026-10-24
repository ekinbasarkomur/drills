"""
2082. The Number of Rich Customers · Easy · https://leetcode.com/problems/the-number-of-rich-customers/
Plan: 30 Days of Pandas · Gün 16 · Statistics

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    store = frame(['bill_id', 'customer_id', 'amount'], [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]], {'bill_id': 'int64', 'customer_id': 'int64', 'amount': 'int64'})
    count_rich_customers(store)
