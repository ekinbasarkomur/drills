"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Plan: Aşama 0 · Linked List

Problem: reverse a singly linked list and return the new head.
Note: you only get one pointer per node, so you must hold onto the next node
      before you overwrite it -- three references is the usual dance.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List, Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head  # TODO


# ---------------------------------------------------------------- tests


def reversed_list(values: List[int]) -> List[int]:
    return to_list(Solution().reverseList(build(values)))


def test_example_1():
    check(reversed_list([0, 1, 2, 3]), [3, 2, 1, 0], "reversed_list([0, 1, 2, 3])")


def test_example_2():
    check(reversed_list([]), [], "reversed_list([])")


def test_single_node():
    check(reversed_list([7]), [7], "reversed_list([7])")


def test_two_nodes():
    check(reversed_list([1, 2]), [2, 1], "reversed_list([1, 2])")


def test_repeated_values():
    check(reversed_list([5, 5, 5]), [5, 5, 5], "reversed_list([5, 5, 5])")


def test_negative_values():
    check(reversed_list([-1, -2, -3]), [-3, -2, -1], "reversed_list([-1, -2, -3])")


def test_value_range_extremes():
    check(reversed_list([-1000, 0, 1000]), [1000, 0, -1000], "reversed_list([-1000, 0, 1000])")


def test_largest_allowed_input():
    # 1000 nodes, the constraint's ceiling.
    check(reversed_list(list(range(1000))), list(range(999, -1, -1)), "reversed_list(list(range(1000)))")


if __name__ == "__main__":
    print(reversed_list([0, 1, 2, 3]))
