"""
19. Remove Nth Node From End of List · Medium · https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Plan: Aşama 0 · Linked List

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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(to_list(Solution().removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5], "to_list(Solution().removeNthFromEnd(build([1, 2, 3, 4, 5]), 2))")


def test_example_2():
    check(to_list(Solution().removeNthFromEnd(build([1]), 1)), [], "to_list(Solution().removeNthFromEnd(build([1]), 1))")


def test_example_3():
    check(to_list(Solution().removeNthFromEnd(build([1, 2]), 1)), [1], "to_list(Solution().removeNthFromEnd(build([1, 2]), 1))")
