"""
641. Design Circular Deque · Medium · https://leetcode.com/problems/design-circular-deque/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MyCircularDeque:

    def __init__(self, k: int):
        raise NotImplementedError
    def insertFront(self, value: int) -> bool:
        raise NotImplementedError
    def insertLast(self, value: int) -> bool:
        raise NotImplementedError
    def deleteFront(self) -> bool:
        raise NotImplementedError
    def deleteLast(self) -> bool:
        raise NotImplementedError
    def getFront(self) -> int:
        raise NotImplementedError
    def getRear(self) -> int:
        raise NotImplementedError
    def isEmpty(self) -> bool:
        raise NotImplementedError
    def isFull(self) -> bool:
        raise NotImplementedError
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MyCircularDeque(3)
    check(obj.insertLast(1), True, "obj.insertLast(1)")
    check(obj.insertLast(2), True, "obj.insertLast(2)")
    check(obj.insertFront(3), True, "obj.insertFront(3)")
    check(obj.insertFront(4), False, "obj.insertFront(4)")
    check(obj.getRear(), 2, "obj.getRear()")
    check(obj.isFull(), True, "obj.isFull()")
    check(obj.deleteLast(), True, "obj.deleteLast()")
    check(obj.insertFront(4), True, "obj.insertFront(4)")
    check(obj.getFront(), 4, "obj.getFront()")
