"""
304. Range Sum Query 2D - Immutable · Medium · https://leetcode.com/problems/range-sum-query-2d-immutable/
Plan: Aşama 1 · Prefix Sum ve Sliding Window

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        raise NotImplementedError
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise NotImplementedError
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    check(obj.sumRegion(2, 1, 4, 3), 8, "obj.sumRegion(2, 1, 4, 3)")
    check(obj.sumRegion(1, 1, 2, 2), 11, "obj.sumRegion(1, 1, 2, 2)")
    check(obj.sumRegion(1, 2, 2, 4), 12, "obj.sumRegion(1, 2, 2, 4)")
