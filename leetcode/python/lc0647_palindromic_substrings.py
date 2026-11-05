"""
647. Palindromic Substrings · Medium · https://leetcode.com/problems/palindromic-substrings/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().countSubstrings('abc'), 3, "Solution().countSubstrings('abc')")


def test_example_2():
    check(Solution().countSubstrings('aaa'), 6, "Solution().countSubstrings('aaa')")
