"""
765. Couples Holding Hands · Hard · https://leetcode.com/problems/couples-holding-hands/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().minSwapsCouples([0, 2, 1, 3]), 1, "Solution().minSwapsCouples([0, 2, 1, 3])")


def test_example_2():
    check(Solution().minSwapsCouples([3, 2, 0, 1]), 0, "Solution().minSwapsCouples([3, 2, 0, 1])")
