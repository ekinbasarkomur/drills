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
    check(Solution().fractionToDecimal(1, 2), '0.5', "Solution().fractionToDecimal(1, 2)")


def test_example_2():
    check(Solution().fractionToDecimal(2, 1), '2', "Solution().fractionToDecimal(2, 1)")


def test_example_3():
    check(Solution().fractionToDecimal(4, 333), '0.(012)', "Solution().fractionToDecimal(4, 333)")
