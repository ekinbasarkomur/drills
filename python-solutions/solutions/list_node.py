"""
Shared singly-linked-list node plus helpers, so linked-list problems can be
written the way LeetCode presents them while the tests stay readable.

    build([1, 2, 3])   -> a list, returns its head (None for [])
    to_list(head)      -> the values, for comparing against an expected list
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
