"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
Plan: Aşama 0 · Stack

Problem: result[i] is how many days you wait after day i for a warmer
         temperature, or 0 if none ever comes.
Note: Days waiting for a warmer day pile up in the order they arrived, and
      the newest one is always resolved first -- a stack of pending indices.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def daily_temperatures(temperatures: List[int]) -> List[int]:
    return Solution().dailyTemperatures(temperatures)


def test_example_1():
    check(daily_temperatures([30, 38, 30, 36, 35, 40, 28]), [1, 4, 1, 2, 1, 0, 0], "daily_temperatures([30, 38, 30, 36, 35, 40, 28])")


def test_example_2():
    # it only ever gets colder
    check(daily_temperatures([22, 21, 20]), [0, 0, 0], "daily_temperatures([22, 21, 20])")


def test_single_day():
    check(daily_temperatures([50]), [0], "daily_temperatures([50])")


def test_two_days_warming():
    check(daily_temperatures([1, 2]), [1, 0], "daily_temperatures([1, 2])")


def test_two_days_cooling():
    check(daily_temperatures([2, 1]), [0, 0], "daily_temperatures([2, 1])")


def test_flat_week():
    # equal is not warmer
    check(daily_temperatures([5, 5, 5]), [0, 0, 0], "daily_temperatures([5, 5, 5])")


def test_the_classic_leetcode_case():
    check(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0], "daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])")


def test_one_warm_day_resolves_everything():
    check(daily_temperatures([1, 1, 1, 100]), [3, 2, 1, 0], "daily_temperatures([1, 1, 1, 100])")


def test_the_warmest_day_is_first():
    check(daily_temperatures([100, 1, 1, 1]), [0, 0, 0, 0], "daily_temperatures([100, 1, 1, 1])")


def test_strictly_ascending():
    check(daily_temperatures([1, 2, 3, 4, 5]), [1, 1, 1, 1, 0], "daily_temperatures([1, 2, 3, 4, 5])")


def test_strictly_descending():
    check(daily_temperatures([5, 4, 3, 2, 1]), [0, 0, 0, 0, 0], "daily_temperatures([5, 4, 3, 2, 1])")


def test_largest_allowed_input():
    # 100_000 days all at 50 except the last at 100: every earlier day waits
    # for that final one. An O(n^2) solution will hang here rather than fail.
    temperatures = [50] * 100_000
    temperatures[99_999] = 100
    expected = [99_999 - i for i in range(100_000)]
    check(daily_temperatures(temperatures), expected, "daily_temperatures(temperatures)")


if __name__ == "__main__":
    print(daily_temperatures([30, 38, 30, 36, 35, 40, 28]))
