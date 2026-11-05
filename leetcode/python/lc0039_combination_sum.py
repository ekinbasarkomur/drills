"""
39. Combination Sum · Medium · https://leetcode.com/problems/combination-sum/
Plan: Aşama 4 · Backtracking

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(deep_sorted(Solution().combinationSum([2, 3, 6, 7], 7)), deep_sorted([[2, 2, 3], [7]]), "deep_sorted(Solution().combinationSum([2, 3, 6, 7], 7))")


def test_example_2():
    check(deep_sorted(Solution().combinationSum([2, 3, 5], 8)), deep_sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]), "deep_sorted(Solution().combinationSum([2, 3, 5], 8))")


def test_example_3():
    check(deep_sorted(Solution().combinationSum([2], 1)), deep_sorted([]), "deep_sorted(Solution().combinationSum([2], 1))")
