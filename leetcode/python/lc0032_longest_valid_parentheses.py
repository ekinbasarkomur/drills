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
    check(Solution().longestValidParentheses('(()'), 2, "Solution().longestValidParentheses('(()')")


def test_example_2():
    check(Solution().longestValidParentheses(')()())'), 4, "Solution().longestValidParentheses(')()())')")


def test_example_3():
    check(Solution().longestValidParentheses(''), 0, "Solution().longestValidParentheses('')")
