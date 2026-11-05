"""
307. Range Sum Query - Mutable · Medium · https://leetcode.com/problems/range-sum-query-mutable/
Plan: Aşama 5 · Segment Tree ve Fenwick

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class NumArray:

    def __init__(self, nums: list[int]):
        raise NotImplementedError
    def update(self, index: int, val: int) -> None:
        raise NotImplementedError
    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = NumArray([1, 3, 5])
    check(obj.sumRange(0, 2), 9, "obj.sumRange(0, 2)")
    obj.update(1, 2)
    check(obj.sumRange(0, 2), 8, "obj.sumRange(0, 2)")
