"""
70. Climbing Stairs · Easy · https://leetcode.com/problems/climbing-stairs/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def climbStairs(self, n: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().climbStairs(2), 2, "Solution().climbStairs(2)")


def test_example_2():
    check(Solution().climbStairs(3), 3, "Solution().climbStairs(3)")
