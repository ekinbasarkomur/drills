"""
608. Tree Node · Medium · https://leetcode.com/problems/tree-node/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tree = frame(['id', 'p_id'], [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]], {'id': 'Int64', 'p_id': 'Int64'})
    check(tree_node(tree), ['id', 'type'], [[1, 'Root'], [2, 'Inner'], [3, 'Leaf'], [4, 'Leaf'], [5, 'Leaf']], ordered=False)


def test_example_2():
    tree = frame(['id', 'p_id'], [[1, None]], {'id': 'Int64', 'p_id': 'Int64'})
    check(tree_node(tree), ['id', 'type'], [[1, 'Root']], ordered=False)
