"""
1326. Minimum Number of Taps to Open to Water a Garden · Hard · https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().minTaps(5, [3, 4, 1, 1, 0, 0]), 1, "Solution().minTaps(5, [3, 4, 1, 1, 0, 0])")


def test_example_2():
    check(Solution().minTaps(3, [0, 0, 0, 0]), -1, "Solution().minTaps(3, [0, 0, 0, 0])")
