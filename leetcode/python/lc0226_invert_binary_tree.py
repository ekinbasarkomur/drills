"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
Plan: Aşama 0 · Trees

Problem: mirror the tree -- every node's left and right swap, all the way
         down -- and return the root.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List, Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root  # TODO


# ---------------------------------------------------------------- tests
# Trees are written in level order; None marks a missing child.


def inverted(values: List[Optional[int]]) -> List[Optional[int]]:
    return to_level_order(Solution().invertTree(build_tree(values)))


def test_example_1():
    check(inverted([1, 2, 3, 4, 5, 6, 7]), [1, 3, 2, 7, 6, 5, 4], "inverted([1, 2, 3, 4, 5, 6, 7])")


def test_example_2():
    check(inverted([3, 2, 1]), [3, 1, 2], "inverted([3, 2, 1])")


def test_example_3():
    check(inverted([]), [], "inverted([])")


def test_single_node():
    check(inverted([1]), [1], "inverted([1])")


def test_only_a_left_child():
    check(inverted([1, 2]), [1, None, 2], "inverted([1, 2])")


def test_only_a_right_child():
    check(inverted([1, None, 2]), [1, 2], "inverted([1, None, 2])")


def test_a_left_leaning_chain_becomes_right_leaning():
    check(inverted([1, 2, None, 3]), [1, None, 2, None, 3], "inverted([1, 2, None, 3])")


def test_lopsided_tree():
    check(inverted([1, 2, 3, None, 4]), [1, 3, 2, None, None, 4], "inverted([1, 2, 3, None, 4])")


def test_negative_values():
    check(inverted([-1, -2, -3]), [-1, -3, -2], "inverted([-1, -2, -3])")


def test_inverting_twice_restores_the_original():
    original = [1, 2, 3, 4, 5, 6, 7]
    check(inverted(inverted(original)), original, "inverted(inverted(original))")


def test_a_symmetric_tree_is_unchanged():
    check(inverted([1, 2, 2]), [1, 2, 2], "inverted([1, 2, 2])")


if __name__ == "__main__":
    print(inverted([1, 2, 3, 4, 5, 6, 7]))
