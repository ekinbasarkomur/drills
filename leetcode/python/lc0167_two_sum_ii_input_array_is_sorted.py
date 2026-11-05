"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Plan: Aşama 0 · Two Pointers

Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
         values that add up to target, smaller index first. Exactly one answer
         exists and you may not use the same element twice.
Follow-up: constant extra space -- so no dict this time.
Approach: two pointers from both ends. The array is sorted, so a sum that is
          too small can only grow by moving left right, and one that is too
          large can only shrink by moving right left.
Time O(n), space O(1)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if target > total:
                left += 1
            elif target < total:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return []
# ---------------------------------------------------------------- tests


def two_sum(numbers: list[int], target: int) -> list[int]:
    return Solution().twoSum(numbers, target)


def test_example_1():
    check(two_sum([1, 2, 3, 4], 3), [1, 2], "two_sum([1, 2, 3, 4], 3)")


def test_example_2():
    check(two_sum([2, 7, 11, 15], 9), [1, 2], "two_sum([2, 7, 11, 15], 9)")


def test_example_3():
    check(two_sum([2, 3, 4], 6), [1, 3], "two_sum([2, 3, 4], 6)")


def test_shortest_possible_input():
    check(two_sum([-1, 0], -1), [1, 2], "two_sum([-1, 0], -1)")


def test_the_two_ends_are_the_answer():
    check(two_sum([1, 5, 6, 7, 20], 21), [1, 5], "two_sum([1, 5, 6, 7, 20], 21)")


def test_the_answer_sits_in_the_middle():
    check(two_sum([1, 4, 5, 6, 20], 11), [3, 4], "two_sum([1, 4, 5, 6, 20], 11)")


def test_equal_values_next_to_each_other():
    check(two_sum([3, 3], 6), [1, 2], "two_sum([3, 3], 6)")


def test_repeated_values_around_the_answer():
    check(two_sum([2, 2, 3, 7], 10), [3, 4], "two_sum([2, 2, 3, 7], 10)")


def test_all_negative():
    check(two_sum([-9, -7, -3, -1], -4), [3, 4], "two_sum([-9, -7, -3, -1], -4)")


def test_crossing_zero():
    check(two_sum([-5, -2, 0, 3, 8], 6), [2, 5], "two_sum([-5, -2, 0, 3, 8], 6)")


def test_target_is_zero():
    check(two_sum([-4, -1, 0, 1, 5], 0), [2, 4], "two_sum([-4, -1, 0, 1, 5], 0)")


def test_value_range_extremes():
    check(two_sum([-1000, 0, 1000], 0), [1, 3], "two_sum([-1000, 0, 1000], 0)")


def test_largest_allowed_input():
    # 1000 elements: the answer is the very first and the very last, so a scan
    # that starts from both ends finds it immediately while a nested loop
    # grinds through the whole array.
    numbers = list(range(1000))
    # 998 + 999 is the only pair reaching 1997, and it sits at the far end
    check(two_sum(numbers, 1997), [999, 1000], "two_sum(numbers, 1997)")


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4], 3))
