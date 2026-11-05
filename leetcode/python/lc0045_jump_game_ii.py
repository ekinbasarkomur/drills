"""
45. Jump Game II · Medium · https://leetcode.com/problems/jump-game-ii/
Plan: Aşama 0 · Greedy

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def jump(self, nums: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().jump([2, 3, 1, 1, 4]), 2, "Solution().jump([2, 3, 1, 1, 4])")


def test_example_2():
    check(Solution().jump([2, 3, 0, 1, 4]), 2, "Solution().jump([2, 3, 0, 1, 4])")
