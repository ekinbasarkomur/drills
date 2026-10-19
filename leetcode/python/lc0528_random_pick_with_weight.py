"""
528. Random Pick with Weight · Medium · https://leetcode.com/problems/random-pick-with-weight/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:

    def __init__(self, w: list[int]):
        raise NotImplementedError
    def pickIndex(self) -> int:
        raise NotImplementedError
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Solution([1])
    obj.pickIndex()


def test_example_2():
    obj = Solution([1, 3])
    obj.pickIndex()
    obj.pickIndex()
    obj.pickIndex()
    obj.pickIndex()
    obj.pickIndex()
