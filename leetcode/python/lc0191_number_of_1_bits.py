"""
191. Number of 1 Bits · Easy · https://leetcode.com/problems/number-of-1-bits/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().hammingWeight(11), 3, "Solution().hammingWeight(11)")


def test_example_2():
    check(Solution().hammingWeight(128), 1, "Solution().hammingWeight(128)")


def test_example_3():
    check(Solution().hammingWeight(2147483645), 30, "Solution().hammingWeight(2147483645)")
