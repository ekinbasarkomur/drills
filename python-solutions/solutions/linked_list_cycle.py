"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Problem: does following next ever revisit a node?
Note: the classic answer walks two pointers at different speeds. If there is a
      loop, the fast one laps the slow one; if not, it runs off the end.
Approach:
Time O(?), space O(?)
"""

from typing import List, Optional

from list_node import ListNode, build


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
    assert has_cycle([1, 2, 3, 4], 1) is True


def test_example_2():
    assert has_cycle([1, 2], -1) is False


def test_empty_list():
    assert has_cycle([], -1) is False


def test_single_node_no_cycle():
    assert has_cycle([1], -1) is False


def test_single_node_pointing_at_itself():
    assert has_cycle([1], 0) is True


def test_cycle_covers_the_whole_list():
    assert has_cycle([1, 2, 3], 0) is True


def test_cycle_is_just_the_last_node():
    assert has_cycle([1, 2, 3], 2) is True


def test_repeated_values_are_not_a_cycle():
    # equal values are not the same node
    assert has_cycle([1, 1, 1, 1], -1) is False


def test_long_list_no_cycle():
    assert has_cycle(list(range(1000)), -1) is False


def test_long_list_with_a_late_cycle():
    assert has_cycle(list(range(1000)), 999) is True


if __name__ == "__main__":
    print(has_cycle([1, 2, 3, 4], 1))
