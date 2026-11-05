"""
98. Validate Binary Search Tree · Medium · https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: TreeNode | None) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().isValidBST(build_tree([2, 1, 3])), True, "Solution().isValidBST(build_tree([2, 1, 3]))")


def test_example_2():
    check(Solution().isValidBST(build_tree([5, 1, 4, None, None, 3, 6])), False, "Solution().isValidBST(build_tree([5, 1, 4, None, None, 3, 6]))")
