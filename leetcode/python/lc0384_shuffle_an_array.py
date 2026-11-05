"""
384. Shuffle an Array · Medium · https://leetcode.com/problems/shuffle-an-array/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:

    def __init__(self, nums: list[int]):
        raise NotImplementedError
    def reset(self) -> list[int]:
        raise NotImplementedError
    def shuffle(self) -> list[int]:
        raise NotImplementedError
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Solution([1, 2, 3])
    obj.shuffle()
    check(obj.reset(), [1, 2, 3], "obj.reset()")
    obj.shuffle()
