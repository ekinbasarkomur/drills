"""
502. IPO · Hard · https://leetcode.com/problems/ipo/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]), 4, "Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])")


def test_example_2():
    check(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]), 6, "Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2])")
