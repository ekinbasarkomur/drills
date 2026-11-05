"""
1146. Snapshot Array · Medium · https://leetcode.com/problems/snapshot-array/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class SnapshotArray:

    def __init__(self, length: int):
        raise NotImplementedError
    def set(self, index: int, val: int) -> None:
        raise NotImplementedError
    def snap(self) -> int:
        raise NotImplementedError
    def get(self, index: int, snap_id: int) -> int:
        raise NotImplementedError
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    check(obj.snap(), 0, "obj.snap()")
    obj.set(0, 6)
    check(obj.get(0, 0), 5, "obj.get(0, 0)")
