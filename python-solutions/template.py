"""
<NUMBER>. <TITLE>            https://leetcode.com/problems/<slug>/

Problem: one or two lines, in your own words.
Approach: the trick in one line. Time O(?), space O(?).
"""


def solve(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError


# ---------------------------------------------------------------- tests
# pytest collects every function named test_*


def test_example_1():
    assert solve([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert solve([3, 2, 4], 6) == [1, 2]


# Scratch area: python solutions/<file>.py runs this, pytest ignores it.
if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))
