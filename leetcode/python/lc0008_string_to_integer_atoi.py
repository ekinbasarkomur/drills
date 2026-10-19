"""
8. String to Integer (atoi) · Medium · https://leetcode.com/problems/string-to-integer-atoi/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def myAtoi(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().myAtoi('42') == 42


def test_example_2():
    assert Solution().myAtoi('   -042') == -42


def test_example_3():
    assert Solution().myAtoi('1337c0d3') == 1337


def test_example_4():
    assert Solution().myAtoi('0-1') == 0


def test_example_5():
    assert Solution().myAtoi('words and 987') == 0
