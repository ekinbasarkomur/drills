"""
393. UTF-8 Validation · Medium · https://leetcode.com/problems/utf-8-validation/
Plan: Aşama 1 · Bit Manipulation

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().validUtf8([197, 130, 1]), True, "Solution().validUtf8([197, 130, 1])")


def test_example_2():
    check(Solution().validUtf8([235, 140, 4]), False, "Solution().validUtf8([235, 140, 4])")
