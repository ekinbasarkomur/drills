"""
94. Binary Tree Inorder Traversal · Easy · https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().inorderTraversal(build_tree([1, None, 2, 3])), [1, 3, 2], "Solution().inorderTraversal(build_tree([1, None, 2, 3]))")


def test_example_2():
    check(Solution().inorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])), [4, 2, 6, 5, 7, 1, 3, 9, 8], "Solution().inorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]))")


def test_example_3():
    check(Solution().inorderTraversal(build_tree([])), [], "Solution().inorderTraversal(build_tree([]))")


def test_example_4():
    check(Solution().inorderTraversal(build_tree([1])), [1], "Solution().inorderTraversal(build_tree([1]))")
