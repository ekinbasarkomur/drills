"""
342. Power of Four · Easy · https://leetcode.com/problems/power-of-four/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().isPowerOfFour(16), True, "Solution().isPowerOfFour(16)")


def test_example_2():
    check(Solution().isPowerOfFour(5), False, "Solution().isPowerOfFour(5)")


def test_example_3():
    check(Solution().isPowerOfFour(1), True, "Solution().isPowerOfFour(1)")
