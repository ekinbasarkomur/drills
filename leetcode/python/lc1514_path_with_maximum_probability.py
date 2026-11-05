"""
1514. Path with Maximum Probability · Medium · https://leetcode.com/problems/path-with-maximum-probability/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2), 0.25), "close(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2), 0.25)")


def test_example_2():
    check_true(close(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2), 0.3), "close(Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2), 0.3)")


def test_example_3():
    check_true(close(Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2), 0.0), "close(Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2), 0.0)")
