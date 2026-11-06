"""
3401. Find Circular Gift Exchange Chains · Hard · https://leetcode.com/problems/find-circular-gift-exchange-chains/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_gift_chains(secret_santa: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    secret_santa = frame(['giver_id', 'receiver_id', 'gift_value'], [[1, 2, 20], [2, 3, 30], [3, 1, 40], [4, 5, 25], [5, 4, 35]], {})
    check(find_gift_chains(secret_santa), ['chain_id', 'chain_length', 'total_gift_value'], [[1, 3, 90], [2, 2, 60]], ordered=True)
