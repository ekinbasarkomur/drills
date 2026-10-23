"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Plan: Aşama 0 · Arrays & Hashing

Problem: length of the longest run of consecutive integers that can be formed
         from nums. Order in the array does not matter. Must run in O(n).
Approach: put everything in a set, then only start counting from a number whose
          predecessor is absent -- that is the head of a run. Each run is walked
          exactly once, so the total work is linear despite the inner while.
          Time O(n), space O(n).
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        single_nums = set()
        inc_map = {}
        max_count = 0

        for num in nums:
            if num in single_nums:
                continue
            single_nums.add(num)

        for num in single_nums:
            if num - 1 in single_nums:
                continue

            inc_map[num] = 1

        for start in inc_map.keys():
            inc = start + 1
            while True:
                if inc in single_nums:
                    inc_map[start] += 1
                    inc += 1
                    continue
                break

            if inc_map[start] > max_count:
                max_count = inc_map[start]

        return max_count
# ---------------------------------------------------------------- tests


def longest(nums: list[int]) -> int:
    return Solution().longestConsecutive(nums)


def test_example_1():
    assert longest([2, 20, 4, 10, 3, 4, 5]) == 4


def test_example_2():
    assert longest([0, 3, 2, 5, 4, 6, 1, 1]) == 7


def test_empty_array():
    assert longest([]) == 0


def test_single_element():
    assert longest([7]) == 1


def test_all_duplicates_of_one_value():
    assert longest([5, 5, 5, 5]) == 1


def test_no_two_numbers_are_consecutive():
    assert longest([10, 30, 50, 70]) == 1


def test_already_sorted():
    assert longest([1, 2, 3, 4, 5]) == 5


def test_given_in_descending_order():
    assert longest([5, 4, 3, 2, 1]) == 5


def test_two_runs_and_the_longer_one_comes_second():
    assert longest([1, 2, 3, 100, 101, 102, 103]) == 4


def test_negative_numbers():
    assert longest([-3, -2, -1, 0, 1]) == 5


def test_run_straddling_zero_with_a_gap():
    assert longest([-5, -4, 100, -3, 7, -1, 0]) == 3


def test_value_range_extremes():
    assert longest([10**9, 10**9 - 1, -(10**9)]) == 2


def test_duplicates_inside_a_run_do_not_inflate_it():
    assert longest([1, 2, 2, 3, 3, 3, 4]) == 4


def test_large_input_stays_linear():
    # 100_000 elements in one unbroken run, handed over shuffled.
    # An O(n^2) solution will hang here rather than fail.
    import random

    n = 100_000
    nums = list(range(n))
    random.Random(0).shuffle(nums)
    assert longest(nums) == n


if __name__ == "__main__":
    print(longest([2, 20, 4, 10, 3, 4, 5]))
