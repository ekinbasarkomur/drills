"""
547. Number of Provinces · Medium · https://leetcode.com/problems/number-of-provinces/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2, "Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])")


def test_example_2():
    check(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3, "Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")
