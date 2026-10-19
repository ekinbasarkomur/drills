"""
150. Evaluate Reverse Polish Notation · Medium · https://leetcode.com/problems/evaluate-reverse-polish-notation/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().evalRPN(['2', '1', '+', '3', '*']) == 9


def test_example_2():
    assert Solution().evalRPN(['4', '13', '5', '/', '+']) == 6


def test_example_3():
    assert Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22
