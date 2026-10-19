"""
2034. Stock Price Fluctuation  · Medium · https://leetcode.com/problems/stock-price-fluctuation/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class StockPrice:

    def __init__(self):
        raise NotImplementedError
    def update(self, timestamp: int, price: int) -> None:
        raise NotImplementedError
    def current(self) -> int:
        raise NotImplementedError
    def maximum(self) -> int:
        raise NotImplementedError
    def minimum(self) -> int:
        raise NotImplementedError
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = StockPrice()
    obj.update(1, 10)
    obj.update(2, 5)
    assert obj.current() == 5
    assert obj.maximum() == 10
    obj.update(1, 3)
    assert obj.maximum() == 5
    obj.update(4, 2)
    assert obj.minimum() == 2
