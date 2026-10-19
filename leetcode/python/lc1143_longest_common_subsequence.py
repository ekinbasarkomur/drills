"""
1143. Longest Common Subsequence · Medium · https://leetcode.com/problems/longest-common-subsequence/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().longestCommonSubsequence('abcde', 'ace') == 3


def test_example_2():
    assert Solution().longestCommonSubsequence('abc', 'abc') == 3


def test_example_3():
    assert Solution().longestCommonSubsequence('abc', 'def') == 0
