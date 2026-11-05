"""
230. Kth Smallest Element in a BST · Medium · https://leetcode.com/problems/kth-smallest-element-in-a-bst/
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
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().kthSmallest(build_tree([3, 1, 4, None, 2]), 1), 1, "Solution().kthSmallest(build_tree([3, 1, 4, None, 2]), 1)")


def test_example_2():
    check(Solution().kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3), 3, "Solution().kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3)")
