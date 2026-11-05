"""
715. Range Module · Hard · https://leetcode.com/problems/range-module/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class RangeModule:

    def __init__(self):
        raise NotImplementedError
    def addRange(self, left: int, right: int) -> None:
        raise NotImplementedError
    def queryRange(self, left: int, right: int) -> bool:
        raise NotImplementedError
    def removeRange(self, left: int, right: int) -> None:
        raise NotImplementedError
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = RangeModule()
    obj.addRange(10, 20)
    obj.removeRange(14, 16)
    check(obj.queryRange(10, 14), True, "obj.queryRange(10, 14)")
    check(obj.queryRange(13, 15), False, "obj.queryRange(13, 15)")
    check(obj.queryRange(16, 17), True, "obj.queryRange(16, 17)")
