"""
3054. Binary Tree Nodes · Medium · https://leetcode.com/problems/binary-tree-nodes/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    tree = frame(['N', 'P'], [[1, 2], [3, 2], [6, 8], [9, 8], [2, 5], [8, 5], [5, None]], {'N': 'Int64', 'P': 'Int64'})
    check(binary_tree_nodes(tree), ['N', 'Type'], [[1, 'Leaf'], [2, 'Inner'], [3, 'Leaf'], [5, 'Root'], [6, 'Leaf'], [8, 'Inner'], [9, 'Leaf']], ordered=True)
