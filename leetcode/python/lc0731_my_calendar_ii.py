"""
731. My Calendar II · Medium · https://leetcode.com/problems/my-calendar-ii/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyCalendarTwo:

    def __init__(self):
        raise NotImplementedError
    def book(self, startTime: int, endTime: int) -> bool:
        raise NotImplementedError
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyCalendarTwo()
    check(obj.book(10, 20), True, "obj.book(10, 20)")
    check(obj.book(50, 60), True, "obj.book(50, 60)")
    check(obj.book(10, 40), True, "obj.book(10, 40)")
    check(obj.book(5, 15), False, "obj.book(5, 15)")
    check(obj.book(5, 10), True, "obj.book(5, 10)")
    check(obj.book(25, 55), True, "obj.book(25, 55)")
