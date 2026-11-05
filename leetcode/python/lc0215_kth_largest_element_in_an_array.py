"""
215. Kth Largest Element in an Array · Medium · https://leetcode.com/problems/kth-largest-element-in-an-array/
Plan: Aşama 0 · Heap & Priority Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5, "Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)")


def test_example_2():
    check(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4, "Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)")
