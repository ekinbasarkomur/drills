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
    check(Solution().consecutiveNumbersSum(5), 2, "Solution().consecutiveNumbersSum(5)")


def test_example_2():
    check(Solution().consecutiveNumbersSum(9), 3, "Solution().consecutiveNumbersSum(9)")


def test_example_3():
    check(Solution().consecutiveNumbersSum(15), 4, "Solution().consecutiveNumbersSum(15)")
