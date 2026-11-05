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
    check(Solution().plusOne([1, 2, 3]), [1, 2, 4], "Solution().plusOne([1, 2, 3])")


def test_example_2():
    check(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2], "Solution().plusOne([4, 3, 2, 1])")


def test_example_3():
    check(Solution().plusOne([9]), [1, 0], "Solution().plusOne([9])")
