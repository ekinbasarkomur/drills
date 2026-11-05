"""
43. Multiply Strings · Medium · https://leetcode.com/problems/multiply-strings/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().multiply('2', '3'), '6', "Solution().multiply('2', '3')")


def test_example_2():
    check(Solution().multiply('123', '456'), '56088', "Solution().multiply('123', '456')")
