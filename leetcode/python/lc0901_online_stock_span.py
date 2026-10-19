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
    assert obj.next(100) == 1
    assert obj.next(80) == 1
    assert obj.next(60) == 1
    assert obj.next(70) == 2
    assert obj.next(60) == 1
    assert obj.next(75) == 4
    assert obj.next(85) == 6
