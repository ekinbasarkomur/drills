"""
877. Stone Game · Medium · https://leetcode.com/problems/stone-game/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().stoneGame([5, 3, 4, 5]), True, "Solution().stoneGame([5, 3, 4, 5])")


def test_example_2():
    check(Solution().stoneGame([3, 7, 2, 3]), True, "Solution().stoneGame([3, 7, 2, 3])")
