"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Plan: Aşama 0 · Trees

Problem: the number of nodes along the longest root-to-leaf path.
         An empty tree has depth 0, a single node has depth 1.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List, Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests
# Trees are written in level order; None marks a missing child.


def depth(values: List[Optional[int]]) -> int:
    return Solution().maxDepth(build_tree(values))


def test_example_1():
    check(depth([1, 2, 3, None, None, 4]), 3, "depth([1, 2, 3, None, None, 4])")


def test_example_2():
    check(depth([]), 0, "depth([])")


def test_single_node():
    check(depth([1]), 1, "depth([1])")


def test_two_levels_full():
    check(depth([1, 2, 3]), 2, "depth([1, 2, 3])")


def test_only_a_left_child():
    check(depth([1, 2]), 2, "depth([1, 2])")


def test_only_a_right_child():
    check(depth([1, None, 2]), 2, "depth([1, None, 2])")


def test_a_left_leaning_chain():
    check(depth([1, 2, None, 3, None, 4]), 4, "depth([1, 2, None, 3, None, 4])")


def test_a_right_leaning_chain():
    check(depth([1, None, 2, None, 3, None, 4]), 4, "depth([1, None, 2, None, 3, None, 4])")


def test_the_deep_side_is_on_the_right():
    check(depth([1, 2, 3, None, None, 4, 5, 6]), 4, "depth([1, 2, 3, None, None, 4, 5, 6])")


def test_a_full_tree_of_three_levels():
    check(depth([1, 2, 3, 4, 5, 6, 7]), 3, "depth([1, 2, 3, 4, 5, 6, 7])")


def test_largest_allowed_input():
    # 100 nodes in a single chain, the constraint's ceiling.
    values: List[Optional[int]] = []
    for i in range(100):
        values.append(i)
        if i < 99:
            values.append(None)
    check(depth(values), 100, "depth(values)")


if __name__ == "__main__":
    print(depth([1, 2, 3, None, None, 4]))
