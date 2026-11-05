"""
315. Count of Smaller Numbers After Self · Hard · https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Plan: Aşama 5 · Segment Tree ve Fenwick

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().countSmaller([5, 2, 6, 1]), [2, 1, 1, 0], "Solution().countSmaller([5, 2, 6, 1])")


def test_example_2():
    check(Solution().countSmaller([-1]), [0], "Solution().countSmaller([-1])")


def test_example_3():
    check(Solution().countSmaller([-1, -1]), [0, 0], "Solution().countSmaller([-1, -1])")
