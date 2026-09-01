"""
36. Valid Sudoku             https://leetcode.com/problems/valid-sudoku/

Problem: a 9x9 board is valid if no row, no column and no 3x3 sub-box holds a
         repeated digit. Empty cells are '.' and the board need not be solvable.
Approach: for each i, gather the i-th row, the i-th column and the i-th sub-box
          into three lists, then check each for a repeat with a set.
          The sub-box index arithmetic walks the nine boxes column-major.
          Time O(81), space O(9).
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def duplicate_exist(array):
            number_inventory = set()
            #print(array)

            for number in array:
                if number == ".":
                    continue

                if number in number_inventory:
                    return True

                number_inventory.add(number)
            return False

        for i in range(0, 9):
            # Check rows:
            row = []
            col = []
            subbox = []
            for j in range(0, 9):
                row.append(board[i][j])

                col.append(board[j][i])

                row_num = (j // 3) + (3 * (i % 3))
                col_num = (j % 3) + (3 * (i // 3))
                subbox.append(board[row_num][col_num])

            if duplicate_exist(row):
                return False
            if duplicate_exist(col):
                return False
            if duplicate_exist(subbox):
                return False

        return True


# ---------------------------------------------------------------- tests
# Boards are written as nine 9-character strings for readability.


def _board(rows: list[str]) -> list[list[str]]:
    assert len(rows) == 9 and all(len(r) == 9 for r in rows)
    return [list(r) for r in rows]


def _valid(rows: list[str]) -> bool:
    return Solution().isValidSudoku(_board(rows))


EXAMPLE_1 = [
    "12..3....",
    "4..5.....",
    ".98.....3",
    "5...6...4",
    "...8.3..5",
    "7...2...6",
    "......2..",
    "...419..8",
    "....8..79",
]

EXAMPLE_2 = [
    "12..3....",
    "4..5.....",
    ".91.....3",
    "5...6...4",
    "...8.3..5",
    "7...2...6",
    "......2..",
    "...419..8",
    "....8..79",
]

EMPTY = ["." * 9] * 9


def test_example_1():
    assert _valid(EXAMPLE_1) is True


def test_example_2():
    # two 1's in the top-left 3x3 sub-box
    assert _valid(EXAMPLE_2) is False


def test_completely_empty_board_is_valid():
    assert _valid(EMPTY) is True


def test_duplicate_in_a_row():
    rows = list(EMPTY)
    rows[0] = "1.......1"
    assert _valid(rows) is False


def test_duplicate_in_a_column_across_different_boxes():
    rows = list(EMPTY)
    rows[0] = "1........"
    rows[4] = "1........"
    assert _valid(rows) is False


def test_duplicate_inside_a_box_only():
    # same box, but different row and different column
    rows = list(EMPTY)
    rows[0] = "1........"
    rows[1] = ".1......."
    assert _valid(rows) is False


def test_same_digit_in_different_row_column_and_box_is_fine():
    rows = list(EMPTY)
    rows[0] = "1........"
    rows[4] = "....1...."
    rows[8] = "........1"
    assert _valid(rows) is True


def test_duplicate_in_the_last_box():
    rows = list(EMPTY)
    rows[7] = ".......9."
    rows[8] = "........9"
    assert _valid(rows) is False


def test_a_solved_board_is_valid():
    assert _valid([
        "534678912",
        "672195348",
        "198342567",
        "859761423",
        "426853791",
        "713924856",
        "961537284",
        "287419635",
        "345286179",
    ]) is True


def test_middle_box_duplicate():
    rows = list(EMPTY)
    rows[3] = "...7....."
    rows[5] = ".....7..."
    assert _valid(rows) is False


if __name__ == "__main__":
    print(_valid(EXAMPLE_1), _valid(EXAMPLE_2))
