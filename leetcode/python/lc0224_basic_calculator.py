"""
224. Basic Calculator · Hard · https://leetcode.com/problems/basic-calculator/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def calculate(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().calculate('1 + 1') == 2


def test_example_2():
    assert Solution().calculate(' 2-1 + 2 ') == 3


def test_example_3():
    assert Solution().calculate('(1+(4+5+2)-3)+(6+8)') == 23
