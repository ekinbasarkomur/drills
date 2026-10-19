"""
136. Single Number · Easy · https://leetcode.com/problems/single-number/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().singleNumber([2, 2, 1]) == 1


def test_example_2():
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4


def test_example_3():
    assert Solution().singleNumber([1]) == 1
