"""
220. Contains Duplicate III · Hard · https://leetcode.com/problems/contains-duplicate-iii/
Plan: Aşama 5 · Segment Tree ve Fenwick

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0), True, "Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)")


def test_example_2():
    check(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3), False, "Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)")
