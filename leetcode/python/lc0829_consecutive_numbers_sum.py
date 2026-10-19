"""
829. Consecutive Numbers Sum · Hard · https://leetcode.com/problems/consecutive-numbers-sum/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().consecutiveNumbersSum(5) == 2


def test_example_2():
    assert Solution().consecutiveNumbersSum(9) == 3


def test_example_3():
    assert Solution().consecutiveNumbersSum(15) == 4
