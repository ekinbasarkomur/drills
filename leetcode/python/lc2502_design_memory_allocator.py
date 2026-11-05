"""
2502. Design Memory Allocator · Medium · https://leetcode.com/problems/design-memory-allocator/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Allocator:

    def __init__(self, n: int):
        raise NotImplementedError
    def allocate(self, size: int, mID: int) -> int:
        raise NotImplementedError
    def freeMemory(self, mID: int) -> int:
        raise NotImplementedError
# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Allocator(10)
    check(obj.allocate(1, 1), 0, "obj.allocate(1, 1)")
    check(obj.allocate(1, 2), 1, "obj.allocate(1, 2)")
    check(obj.allocate(1, 3), 2, "obj.allocate(1, 3)")
    check(obj.freeMemory(2), 1, "obj.freeMemory(2)")
    check(obj.allocate(3, 4), 3, "obj.allocate(3, 4)")
    check(obj.allocate(1, 1), 1, "obj.allocate(1, 1)")
    check(obj.allocate(1, 1), 6, "obj.allocate(1, 1)")
    check(obj.freeMemory(1), 3, "obj.freeMemory(1)")
    check(obj.allocate(10, 2), -1, "obj.allocate(10, 2)")
    check(obj.freeMemory(7), 0, "obj.freeMemory(7)")
