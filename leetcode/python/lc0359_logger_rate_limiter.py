"""
359. Logger Rate Limiter · Easy · https://leetcode.com/problems/logger-rate-limiter/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Logger:

    def __init__(self):
        raise NotImplementedError
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    obj = Logger()
    obj.shouldPrintMessage(1, 'foo')
    obj.shouldPrintMessage(2, 'bar')
    obj.shouldPrintMessage(3, 'foo')
    obj.shouldPrintMessage(8, 'bar')
    obj.shouldPrintMessage(10, 'foo')
    obj.shouldPrintMessage(11, 'foo')
