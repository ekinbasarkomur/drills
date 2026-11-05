"""
55. Jump Game · Medium · https://leetcode.com/problems/jump-game/
Plan: Aşama 0 · Greedy

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().canJump([2, 3, 1, 1, 4]), True, "Solution().canJump([2, 3, 1, 1, 4])")


def test_example_2():
    check(Solution().canJump([3, 2, 1, 0, 4]), False, "Solution().canJump([3, 2, 1, 0, 4])")
