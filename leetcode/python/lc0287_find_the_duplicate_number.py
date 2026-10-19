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
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2


def test_example_2():
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3


def test_example_3():
    assert Solution().findDuplicate([3, 3, 3, 3, 3]) == 3
