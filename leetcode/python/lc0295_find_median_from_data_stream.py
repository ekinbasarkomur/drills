"""
295. Find Median from Data Stream · Hard · https://leetcode.com/problems/find-median-from-data-stream/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MedianFinder:

    def __init__(self):
        raise NotImplementedError
    def addNum(self, num: int) -> None:
        raise NotImplementedError
    def findMedian(self) -> float:
        raise NotImplementedError
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert close(obj.findMedian(), 1.5)
    obj.addNum(3)
    assert close(obj.findMedian(), 2.0)
