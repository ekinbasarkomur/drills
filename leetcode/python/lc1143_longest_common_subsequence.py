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
    check(Solution().longestCommonSubsequence('abcde', 'ace'), 3, "Solution().longestCommonSubsequence('abcde', 'ace')")


def test_example_2():
    check(Solution().longestCommonSubsequence('abc', 'abc'), 3, "Solution().longestCommonSubsequence('abc', 'abc')")


def test_example_3():
    check(Solution().longestCommonSubsequence('abc', 'def'), 0, "Solution().longestCommonSubsequence('abc', 'def')")
