"""
543. Diameter of Binary Tree · Easy · https://leetcode.com/problems/diameter-of-binary-tree/
Plan: Aşama 0 · Trees

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3


def test_example_2():
    assert Solution().diameterOfBinaryTree(build_tree([1, 2])) == 1
