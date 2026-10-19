"""
166. Fraction to Recurring Decimal · Medium · https://leetcode.com/problems/fraction-to-recurring-decimal/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().fractionToDecimal(1, 2) == '0.5'


def test_example_2():
    assert Solution().fractionToDecimal(2, 1) == '2'


def test_example_3():
    assert Solution().fractionToDecimal(4, 333) == '0.(012)'
