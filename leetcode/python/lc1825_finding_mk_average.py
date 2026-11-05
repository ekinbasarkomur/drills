"""
1825. Finding MK Average · Hard · https://leetcode.com/problems/finding-mk-average/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MKAverage:

    def __init__(self, m: int, k: int):
        raise NotImplementedError
    def addElement(self, num: int) -> None:
        raise NotImplementedError
    def calculateMKAverage(self) -> int:
        raise NotImplementedError
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    check(obj.calculateMKAverage(), -1, "obj.calculateMKAverage()")
    obj.addElement(10)
    check(obj.calculateMKAverage(), 3, "obj.calculateMKAverage()")
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    check(obj.calculateMKAverage(), 5, "obj.calculateMKAverage()")
