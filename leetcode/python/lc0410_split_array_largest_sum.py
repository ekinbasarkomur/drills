"""
410. Split Array Largest Sum · Hard · https://leetcode.com/problems/split-array-largest-sum/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().splitArray([7, 2, 5, 10, 8], 2) == 18


def test_example_2():
    assert Solution().splitArray([1, 2, 3, 4, 5], 2) == 9
