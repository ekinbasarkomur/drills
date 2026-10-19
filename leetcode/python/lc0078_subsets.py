"""
78. Subsets · Medium · https://leetcode.com/problems/subsets/
Plan: Aşama 4 · Backtracking

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert deep_sorted(Solution().subsets([1, 2, 3])) == deep_sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


def test_example_2():
    assert deep_sorted(Solution().subsets([0])) == deep_sorted([[], [0]])
