"""
371. Sum of Two Integers · Medium · https://leetcode.com/problems/sum-of-two-integers/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def getSum(self, a: int, b: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().getSum(1, 2), 3, "Solution().getSum(1, 2)")


def test_example_2():
    check(Solution().getSum(2, 3), 5, "Solution().getSum(2, 3)")
