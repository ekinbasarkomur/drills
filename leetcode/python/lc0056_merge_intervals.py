"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Plan: Aşama 0 · Intervals

Problem: merge every pair of intervals that share at least one point, and
         return the non-overlapping intervals that cover the same ground.
         Touching counts as overlapping: [1,2] and [2,3] become [1,3].
Note: the input is NOT sorted, and that is the whole trick -- once it is,
      one pass is enough because only the previous interval can overlap.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests
# "You may return the answer in any order" -> sort before comparing.


def merge(intervals: list[list[int]]) -> list[list[int]]:
    return sorted(Solution().merge([list(p) for p in intervals]))


def expect(intervals: list[list[int]]) -> list[list[int]]:
    return sorted(list(p) for p in intervals)


def test_example_1():
    check(merge([[1, 3], [1, 5], [6, 7]]), expect([[1, 5], [6, 7]]), "merge([[1, 3], [1, 5], [6, 7]])")


def test_example_2():
    # touching at a single point still merges
    check(merge([[1, 2], [2, 3]]), expect([[1, 3]]), "merge([[1, 2], [2, 3]])")


def test_a_single_interval():
    check(merge([[1, 4]]), expect([[1, 4]]), "merge([[1, 4]])")


def test_nothing_overlaps():
    check(merge([[1, 4], [5, 6]]), expect([[1, 4], [5, 6]]), "merge([[1, 4], [5, 6]])")


def test_one_interval_swallows_the_rest():
    check(merge([[1, 10], [2, 3], [4, 5]]), expect([[1, 10]]), "merge([[1, 10], [2, 3], [4, 5]])")


def test_input_arrives_out_of_order():
    check(merge([[5, 6], [1, 2], [3, 4]]), expect([[1, 2], [3, 4], [5, 6]]), "merge([[5, 6], [1, 2], [3, 4]])")


def test_a_zero_length_interval():
    check(merge([[0, 0]]), expect([[0, 0]]), "merge([[0, 0]])")


def test_identical_intervals_collapse():
    check(merge([[1, 1], [1, 1]]), expect([[1, 1]]), "merge([[1, 1], [1, 1]])")


def test_value_range_extremes():
    check(merge([[0, 1000]]), expect([[0, 1000]]), "merge([[0, 1000]])")


def test_a_chain_that_merges_end_to_end():
    check(merge([[1, 2], [2, 3], [3, 4], [4, 5]]), expect([[1, 5]]), "merge([[1, 2], [2, 3], [3, 4], [4, 5]])")


def test_largest_allowed_input_all_merge():
    # 1000 intervals all starting at 0: they collapse to one.
    check(merge([[0, i] for i in range(1000)]), expect([[0, 999]]), "merge([[0, i] for i in range(1000)])")


def test_largest_allowed_input_none_merge():
    # 500 intervals with a gap between each: nothing collapses.
    check(len(merge([[i * 2, i * 2] for i in range(500)])), 500, "len(merge([[i * 2, i * 2] for i in range(500)]))")


if __name__ == "__main__":
    print(merge([[1, 3], [1, 5], [6, 7]]))
