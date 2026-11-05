"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
Plan: Aşama 0 · Linked List

Problem: does following next ever revisit a node?
Note: the classic answer walks two pointers at different speeds. If there is a
      loop, the fast one laps the slow one; if not, it runs off the end.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List, Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return False  # TODO


# ---------------------------------------------------------------- tests
# A cycle is made by pointing the tail at the index-th node; index -1 means no
# cycle.


def has_cycle(values: List[int], index: int) -> bool:
    head = build(values)

    tail = head
    while tail and tail.next:
        tail = tail.next

    if index >= 0 and tail:
        target = head
        for _ in range(index):
            target = target.next
        tail.next = target

    return Solution().hasCycle(head)


def test_example_1():
    check(has_cycle([1, 2, 3, 4], 1), True, "has_cycle([1, 2, 3, 4], 1)", op="is")


def test_example_2():
    check(has_cycle([1, 2], -1), False, "has_cycle([1, 2], -1)", op="is")


def test_empty_list():
    check(has_cycle([], -1), False, "has_cycle([], -1)", op="is")


def test_single_node_no_cycle():
    check(has_cycle([1], -1), False, "has_cycle([1], -1)", op="is")


def test_single_node_pointing_at_itself():
    check(has_cycle([1], 0), True, "has_cycle([1], 0)", op="is")


def test_cycle_covers_the_whole_list():
    check(has_cycle([1, 2, 3], 0), True, "has_cycle([1, 2, 3], 0)", op="is")


def test_cycle_is_just_the_last_node():
    check(has_cycle([1, 2, 3], 2), True, "has_cycle([1, 2, 3], 2)", op="is")


def test_repeated_values_are_not_a_cycle():
    # equal values are not the same node
    check(has_cycle([1, 1, 1, 1], -1), False, "has_cycle([1, 1, 1, 1], -1)", op="is")


def test_long_list_no_cycle():
    check(has_cycle(list(range(1000)), -1), False, "has_cycle(list(range(1000)), -1)", op="is")


def test_long_list_with_a_late_cycle():
    check(has_cycle(list(range(1000)), 999), True, "has_cycle(list(range(1000)), 999)", op="is")


if __name__ == "__main__":
    print(has_cycle([1, 2, 3, 4], 1))
