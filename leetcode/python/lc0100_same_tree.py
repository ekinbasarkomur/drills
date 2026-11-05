"""
100. Same Tree · Easy · https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])), True, "Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3]))")


def test_example_2():
    check(Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2])), False, "Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2]))")


def test_example_3():
    check(Solution().isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])), False, "Solution().isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2]))")
