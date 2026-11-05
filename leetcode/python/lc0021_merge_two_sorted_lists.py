"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Plan: Aşama 0 · Linked List

Problem: splice two sorted lists into one sorted list, reusing the nodes.
Note: a dummy head node saves you from special-casing "which list has the
      first element" before the loop even starts.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List, Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return list1  # TODO


# ---------------------------------------------------------------- tests


def merged(a: List[int], b: List[int]) -> List[int]:
    return to_list(Solution().mergeTwoLists(build(a), build(b)))


def test_example_1():
    check(merged([1, 2, 4], [1, 3, 5]), [1, 1, 2, 3, 4, 5], "merged([1, 2, 4], [1, 3, 5])")


def test_example_2():
    check(merged([], [1, 2]), [1, 2], "merged([], [1, 2])")


def test_example_3():
    check(merged([], []), [], "merged([], [])")


def test_first_list_empty():
    check(merged([], [5]), [5], "merged([], [5])")


def test_second_list_empty():
    check(merged([5], []), [5], "merged([5], [])")


def test_one_list_entirely_precedes_the_other():
    check(merged([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6], "merged([1, 2, 3], [4, 5, 6])")
    check(merged([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6], "merged([4, 5, 6], [1, 2, 3])")


def test_perfectly_interleaved():
    check(merged([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "merged([1, 3, 5], [2, 4, 6])")


def test_all_values_equal():
    check(merged([2, 2], [2, 2]), [2, 2, 2, 2], "merged([2, 2], [2, 2])")


def test_very_different_lengths():
    check(merged([1], [2, 3, 4, 5]), [1, 2, 3, 4, 5], "merged([1], [2, 3, 4, 5])")


def test_negative_values():
    check(merged([-5, -1], [-3, 0]), [-5, -3, -1, 0], "merged([-5, -1], [-3, 0])")


def test_value_range_extremes():
    check(merged([-100, 100], [0]), [-100, 0, 100], "merged([-100, 100], [0])")


def test_largest_allowed_input():
    # 100 nodes each, the constraint's ceiling.
    a = [i * 2 for i in range(100)]
    b = [i * 2 + 1 for i in range(100)]
    check(merged(a, b), list(range(200)), "merged(a, b)")


if __name__ == "__main__":
    print(merged([1, 2, 4], [1, 3, 5]))
