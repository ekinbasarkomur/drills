"""
66. Plus One · Easy · https://leetcode.com/problems/plus-one/
Plan: Aşama 0 · Math

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]


def test_example_2():
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_example_3():
    assert Solution().plusOne([9]) == [1, 0]
