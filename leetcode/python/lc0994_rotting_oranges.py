"""
994. Rotting Oranges · Medium · https://leetcode.com/problems/rotting-oranges/
Plan: Aşama 0 · Graphs

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4, "Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])")


def test_example_2():
    check(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1, "Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])")


def test_example_3():
    check(Solution().orangesRotting([[0, 2]]), 0, "Solution().orangesRotting([[0, 2]])")
