"""
732. My Calendar III · Hard · https://leetcode.com/problems/my-calendar-iii/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyCalendarThree:

    def __init__(self):
        raise NotImplementedError
    def book(self, startTime: int, endTime: int) -> int:
        raise NotImplementedError
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyCalendarThree()
    check(obj.book(10, 20), 1, "obj.book(10, 20)")
    check(obj.book(50, 60), 1, "obj.book(50, 60)")
    check(obj.book(10, 40), 2, "obj.book(10, 40)")
    check(obj.book(5, 15), 3, "obj.book(5, 15)")
    check(obj.book(5, 10), 3, "obj.book(5, 10)")
    check(obj.book(25, 55), 3, "obj.book(25, 55)")
