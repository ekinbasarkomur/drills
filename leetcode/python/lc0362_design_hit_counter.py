"""
362. Design Hit Counter · Medium · https://leetcode.com/problems/design-hit-counter/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class HitCounter:

    def __init__(self):
        raise NotImplementedError
    def hit(self, timestamp: int) -> None:
        raise NotImplementedError
    def getHits(self, timestamp: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    obj.getHits(4)
    obj.hit(300)
    obj.getHits(300)
    obj.getHits(301)
