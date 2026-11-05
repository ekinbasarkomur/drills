"""
232. Implement Queue using Stacks · Easy · https://leetcode.com/problems/implement-queue-using-stacks/
Plan: Aşama 0 · Stack

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyQueue:

    def __init__(self):
        raise NotImplementedError
    def push(self, x: int) -> None:
        raise NotImplementedError
    def pop(self) -> int:
        raise NotImplementedError
    def peek(self) -> int:
        raise NotImplementedError
    def empty(self) -> bool:
        raise NotImplementedError
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    check(obj.peek(), 1, "obj.peek()")
    check(obj.pop(), 1, "obj.pop()")
    check(obj.empty(), False, "obj.empty()")
