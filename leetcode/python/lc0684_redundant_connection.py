"""
684. Redundant Connection · Medium · https://leetcode.com/problems/redundant-connection/
Plan: Aşama 0 · Graphs

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3], "Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])")


def test_example_2():
    check(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4], "Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])")
