"""
1319. Number of Operations to Make Network Connected · Medium · https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().makeConnected(4, [[0, 1], [0, 2], [1, 2]]), 1, "Solution().makeConnected(4, [[0, 1], [0, 2], [1, 2]])")


def test_example_2():
    check(Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]), 2, "Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])")


def test_example_3():
    check(Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]), -1, "Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]])")
