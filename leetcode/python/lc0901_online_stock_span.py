"""
901. Online Stock Span · Medium · https://leetcode.com/problems/online-stock-span/
Plan: Aşama 1 · Monotonic Stack ve Queue

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class StockSpanner:

    def __init__(self):
        raise NotImplementedError
    def next(self, price: int) -> int:
        raise NotImplementedError
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = StockSpanner()
    check(obj.next(100), 1, "obj.next(100)")
    check(obj.next(80), 1, "obj.next(80)")
    check(obj.next(60), 1, "obj.next(60)")
    check(obj.next(70), 2, "obj.next(70)")
    check(obj.next(60), 1, "obj.next(60)")
    check(obj.next(75), 4, "obj.next(75)")
    check(obj.next(85), 6, "obj.next(85)")
