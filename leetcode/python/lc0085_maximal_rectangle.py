"""
85. Maximal Rectangle · Hard · https://leetcode.com/problems/maximal-rectangle/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().maximalRectangle([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]), 6, "Solution().maximalRectangle([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']])")


def test_example_2():
    check(Solution().maximalRectangle([['0']]), 0, "Solution().maximalRectangle([['0']])")


def test_example_3():
    check(Solution().maximalRectangle([['1']]), 1, "Solution().maximalRectangle([['1']])")
