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
    assert Solution().isPowerOfFour(16) == True


def test_example_2():
    assert Solution().isPowerOfFour(5) == False


def test_example_3():
    assert Solution().isPowerOfFour(1) == True
