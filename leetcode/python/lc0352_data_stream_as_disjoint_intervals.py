"""
352. Data Stream as Disjoint Intervals · Hard · https://leetcode.com/problems/data-stream-as-disjoint-intervals/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class SummaryRanges:

    def __init__(self):
        raise NotImplementedError
    def addNum(self, value: int) -> None:
        raise NotImplementedError
    def getIntervals(self) -> list[list[int]]:
        raise NotImplementedError
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = SummaryRanges()
    obj.addNum(1)
    assert obj.getIntervals() == [[1, 1]]
    obj.addNum(3)
    assert obj.getIntervals() == [[1, 1], [3, 3]]
    obj.addNum(7)
    assert obj.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    obj.addNum(2)
    assert obj.getIntervals() == [[1, 3], [7, 7]]
    obj.addNum(6)
    assert obj.getIntervals() == [[1, 3], [6, 7]]
