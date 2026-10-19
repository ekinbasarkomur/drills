"""
221. Maximal Square · Medium · https://leetcode.com/problems/maximal-square/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().maximalSquare([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]) == 4


def test_example_2():
    assert Solution().maximalSquare([['0', '1'], ['1', '0']]) == 1


def test_example_3():
    assert Solution().maximalSquare([['0']]) == 0
