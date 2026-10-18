"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Problem: count the connected groups of '1' cells in the grid. Cells join
         horizontally and vertically only, never diagonally.
Note: Once you reach a land cell, sink the whole island before moving on --
      otherwise you count the same island once per cell.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def num_islands(grid: List[List[str]]) -> int:
    return Solution().numIslands(grid)


def test_example_1():
    assert num_islands([list("01110"), list("01010"), list("11000"), list("00000")]) == 1


def test_example_2():
    assert num_islands([list("11001"), list("11001"), list("00100"), list("00011")]) == 4


def test_all_water():
    assert num_islands([list("000"), list("000")]) == 0


def test_all_land():
    assert num_islands([list("111"), list("111")]) == 1


def test_single_cell_land():
    assert num_islands(["1"]) == 1


def test_single_cell_water():
    assert num_islands(["0"]) == 0


def test_one_row():
    assert num_islands([list("10101")]) == 3


def test_one_column():
    assert num_islands(["1", "0", "1", "1"]) == 2


def test_diagonals_do_not_connect():
    # touching corners is not adjacency
    assert num_islands([list("10"), list("01")]) == 2


def test_a_ring_of_land_around_water():
    assert num_islands([list("111"), list("101"), list("111")]) == 1


def test_checkerboard():
    assert num_islands([list("101"), list("010"), list("101")]) == 5


def test_largest_allowed_input():
    # 100x100 checkerboard, the constraint's ceiling: 2500 single-cell
    # islands, none of them touching.
    grid = [["1" if (r + c) % 2 == 0 else "0" for c in range(100)] for r in range(100)]
    assert num_islands(grid) == 2_500
    assert num_islands([]) == 2500


if __name__ == "__main__":
    print(num_islands([list("01110"), list("01010"), list("11000"), list("00000")]))
