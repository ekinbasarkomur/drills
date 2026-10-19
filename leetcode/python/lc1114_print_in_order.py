"""
1114. Print in Order · Easy · https://leetcode.com/problems/print-in-order/
Plan: Aşama 5 · Concurrency

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Foo:
    def __init__(self):
        raise NotImplementedError
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


# ---------------------------------------------------------------- tests

# No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
# Write your own below if you want a local check.
