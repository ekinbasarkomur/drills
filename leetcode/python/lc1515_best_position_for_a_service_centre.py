"""
1515. Best Position for a Service Centre · Hard · https://leetcode.com/problems/best-position-for-a-service-centre/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]), 4.0), "close(Solution().getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]), 4.0)")


def test_example_2():
    check_true(close(Solution().getMinDistSum([[1, 1], [3, 3]]), 2.82843), "close(Solution().getMinDistSum([[1, 1], [3, 3]]), 2.82843)")
