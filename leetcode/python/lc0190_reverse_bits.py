"""
190. Reverse Bits · Easy · https://leetcode.com/problems/reverse-bits/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def reverseBits(self, n: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().reverseBits(43261596) == 964176192


def test_example_2():
    assert Solution().reverseBits(2147483644) == 1073741822
