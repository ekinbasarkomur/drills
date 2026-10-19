"""
2484. Count Palindromic Subsequences · Hard · https://leetcode.com/problems/count-palindromic-subsequences/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def countPalindromes(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().countPalindromes('103301') == 2


def test_example_2():
    assert Solution().countPalindromes('0000000') == 21


def test_example_3():
    assert Solution().countPalindromes('9999900000') == 2
