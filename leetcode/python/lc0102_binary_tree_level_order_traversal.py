"""
102. Binary Tree Level Order Traversal · Medium · https://leetcode.com/problems/binary-tree-level-order-traversal/
Plan: Aşama 2 · Tree

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]


def test_example_2():
    assert Solution().levelOrder(build_tree([1])) == [[1]]


def test_example_3():
    assert Solution().levelOrder(build_tree([])) == []
