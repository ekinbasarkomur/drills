"""
303. Range Sum Query - Immutable · Easy · https://leetcode.com/problems/range-sum-query-immutable/
Plan: Aşama 1 · Prefix Sum ve Sliding Window

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class NumArray:

    def __init__(self, nums: list[int]):
        raise NotImplementedError
    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    check(obj.sumRange(0, 2), 1, "obj.sumRange(0, 2)")
    check(obj.sumRange(2, 5), -1, "obj.sumRange(2, 5)")
    check(obj.sumRange(0, 5), -3, "obj.sumRange(0, 5)")
