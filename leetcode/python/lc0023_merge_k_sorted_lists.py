"""
23. Merge k Sorted Lists · Hard · https://leetcode.com/problems/merge-k-sorted-lists/
Plan: Aşama 2 · Data Stream ve Heap

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
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert to_list(Solution().mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_example_2():
    assert to_list(Solution().mergeKLists([])) == []


def test_example_3():
    assert to_list(Solution().mergeKLists([build([])])) == []
