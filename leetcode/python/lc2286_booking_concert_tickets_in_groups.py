"""
2286. Booking Concert Tickets in Groups · Hard · https://leetcode.com/problems/booking-concert-tickets-in-groups/
Plan: Aşama 5 · Segment Tree ve Fenwick

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class BookMyShow:

    def __init__(self, n: int, m: int):
        raise NotImplementedError
    def gather(self, k: int, maxRow: int) -> list[int]:
        raise NotImplementedError
    def scatter(self, k: int, maxRow: int) -> bool:
        raise NotImplementedError
# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = BookMyShow(2, 5)
    check(obj.gather(4, 0), [0, 0], "obj.gather(4, 0)")
    check(obj.gather(2, 0), [], "obj.gather(2, 0)")
    check(obj.scatter(5, 1), True, "obj.scatter(5, 1)")
    check(obj.scatter(5, 1), False, "obj.scatter(5, 1)")
