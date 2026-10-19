"""
622. Design Circular Queue · Medium · https://leetcode.com/problems/design-circular-queue/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyCircularQueue:

    def __init__(self, k: int):
        raise NotImplementedError
    def enQueue(self, value: int) -> bool:
        raise NotImplementedError
    def deQueue(self) -> bool:
        raise NotImplementedError
    def Front(self) -> int:
        raise NotImplementedError
    def Rear(self) -> int:
        raise NotImplementedError
    def isEmpty(self) -> bool:
        raise NotImplementedError
    def isFull(self) -> bool:
        raise NotImplementedError
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyCircularQueue(3)
    assert obj.enQueue(1) == True
    assert obj.enQueue(2) == True
    assert obj.enQueue(3) == True
    assert obj.enQueue(4) == False
    assert obj.Rear() == 3
    assert obj.isFull() == True
    assert obj.deQueue() == True
    assert obj.enQueue(4) == True
    assert obj.Rear() == 4
