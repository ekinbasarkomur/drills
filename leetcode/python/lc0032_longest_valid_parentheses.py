"""
32. Longest Valid Parentheses · Hard · https://leetcode.com/problems/longest-valid-parentheses/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().longestValidParentheses('(()') == 2


def test_example_2():
    assert Solution().longestValidParentheses(')()())') == 4


def test_example_3():
    assert Solution().longestValidParentheses('') == 0
