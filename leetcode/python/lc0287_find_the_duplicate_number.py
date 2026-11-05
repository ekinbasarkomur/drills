"""
287. Find the Duplicate Number · Medium · https://leetcode.com/problems/find-the-duplicate-number/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findDuplicate([1, 3, 4, 2, 2]), 2, "Solution().findDuplicate([1, 3, 4, 2, 2])")


def test_example_2():
    check(Solution().findDuplicate([3, 1, 3, 4, 2]), 3, "Solution().findDuplicate([3, 1, 3, 4, 2])")


def test_example_3():
    check(Solution().findDuplicate([3, 3, 3, 3, 3]), 3, "Solution().findDuplicate([3, 3, 3, 3, 3])")
