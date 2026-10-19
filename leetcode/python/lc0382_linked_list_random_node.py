"""
382. Linked List Random Node · Medium · https://leetcode.com/problems/linked-list-random-node/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        raise NotImplementedError
    def getRandom(self) -> int:
        raise NotImplementedError
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Solution(build([1, 2, 3]))
    obj.getRandom()
    obj.getRandom()
    obj.getRandom()
    obj.getRandom()
    obj.getRandom()
