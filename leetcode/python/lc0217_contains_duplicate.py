"""
217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/
Plan: Aşama 0 · Arrays & Hashing

Problem: return True if any value appears more than once in nums.
Approach: walk the array once, keep every number seen so far in a set.
          Time O(n), space O(n).
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# ---------------------------------------------------------------- tests

# The tests below call the old free functions; forward them to Solution.
def has_duplicate(*args): return Solution().containsDuplicate(*args)  # noqa: E704


def test_example_1():
    check(has_duplicate([1, 2, 3, 3]), True, "has_duplicate([1, 2, 3, 3])", op="is")


def test_example_2():
    check(has_duplicate([1, 2, 3, 4]), False, "has_duplicate([1, 2, 3, 4])", op="is")


def test_empty_array():
    check(has_duplicate([]), False, "has_duplicate([])", op="is")


def test_single_element():
    check(has_duplicate([7]), False, "has_duplicate([7])", op="is")


def test_duplicate_at_the_very_end():
    check(has_duplicate([1, 2, 3, 4, 5, 1]), True, "has_duplicate([1, 2, 3, 4, 5, 1])", op="is")


def test_negatives_and_extremes():
    check(has_duplicate([-10**9, 0, -10**9]), True, "has_duplicate([-10**9, 0, -10**9])", op="is")
    check(has_duplicate([-10**9, 10**9]), False, "has_duplicate([-10**9, 10**9])", op="is")


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 3]))
