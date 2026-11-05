"""
729. My Calendar I · Medium · https://leetcode.com/problems/my-calendar-i/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyCalendar:

    def __init__(self):
        raise NotImplementedError
    def book(self, startTime: int, endTime: int) -> bool:
        raise NotImplementedError
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyCalendar()
    check(obj.book(10, 20), True, "obj.book(10, 20)")
    check(obj.book(15, 25), False, "obj.book(15, 25)")
    check(obj.book(20, 30), True, "obj.book(20, 30)")
