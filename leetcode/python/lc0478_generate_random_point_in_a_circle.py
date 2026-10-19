"""
478. Generate Random Point in a Circle · Medium · https://leetcode.com/problems/generate-random-point-in-a-circle/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        raise NotImplementedError
    def randPoint(self) -> list[float]:
        raise NotImplementedError
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Solution(1.0, 0.0, 0.0)
    assert close(obj.randPoint(), [-0.02493, -0.38077])
    assert close(obj.randPoint(), [0.82314, 0.38945])
    assert close(obj.randPoint(), [0.36572, 0.17248])
