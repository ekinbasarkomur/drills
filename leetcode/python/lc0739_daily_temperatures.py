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
    assert daily_temperatures([30, 38, 30, 36, 35, 40, 28]) == [1, 4, 1, 2, 1, 0, 0]


def test_example_2():
    # it only ever gets colder
    assert daily_temperatures([22, 21, 20]) == [0, 0, 0]


def test_single_day():
    assert daily_temperatures([50]) == [0]


def test_two_days_warming():
    assert daily_temperatures([1, 2]) == [1, 0]


def test_two_days_cooling():
    assert daily_temperatures([2, 1]) == [0, 0]


def test_flat_week():
    # equal is not warmer
    assert daily_temperatures([5, 5, 5]) == [0, 0, 0]


def test_the_classic_leetcode_case():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_one_warm_day_resolves_everything():
    assert daily_temperatures([1, 1, 1, 100]) == [3, 2, 1, 0]


def test_the_warmest_day_is_first():
    assert daily_temperatures([100, 1, 1, 1]) == [0, 0, 0, 0]


def test_strictly_ascending():
    assert daily_temperatures([1, 2, 3, 4, 5]) == [1, 1, 1, 1, 0]


def test_strictly_descending():
    assert daily_temperatures([5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0]


def test_largest_allowed_input():
    # 100_000 days all at 50 except the last at 100: every earlier day waits
    # for that final one. An O(n^2) solution will hang here rather than fail.
    temperatures = [50] * 100_000
    temperatures[99_999] = 100
    expected = [99_999 - i for i in range(100_000)]
    assert daily_temperatures(temperatures) == expected


if __name__ == "__main__":
    print(daily_temperatures([30, 38, 30, 36, 35, 40, 28]))
