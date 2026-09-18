// 36. Valid Sudoku             https://leetcode.com/problems/valid-sudoku/
//
// Problem: a 9x9 board is valid if no row, no column and no 3x3 sub-box holds a
//          repeated digit. Empty cells are '.' and the board need not be
//          solvable, or even full.
// Approach:
// Time O(?), space O(?)

#include <array>
#include <string>
#include <vector>

#include "test.hpp"

bool isValidSudoku(const std::vector<std::vector<char>> &board) {
    (void)board;
    return false; // TODO
}

// ---------------------------------------------------------------- tests
// Boards are written as nine 9-character strings for readability.

using Rows = std::array<std::string, 9>;

static bool valid(const Rows &rows) {
    std::vector<std::vector<char>> board;
    for (const auto &row : rows) {
        CHECK(row.size() == 9);
        board.emplace_back(row.begin(), row.end());
    }
    return isValidSudoku(board);
}

static Rows empty_board() {
    Rows rows;
    for (auto &row : rows)
        row = ".........";
    return rows;
}

static const Rows EXAMPLE_1 = {"12..3....", "4..5.....", ".98.....3",
                               "5...6...4", "...8.3..5", "7...2...6",
                               "......2..", "...419..8", "....8..79"};

static const Rows EXAMPLE_2 = {"12..3....", "4..5.....", ".91.....3",
                               "5...6...4", "...8.3..5", "7...2...6",
                               "......2..", "...419..8", "....8..79"};

TEST(example_1) { CHECK(valid(EXAMPLE_1)); }

TEST(example_2) {
    // two 1's in the top-left 3x3 sub-box
    CHECK(!valid(EXAMPLE_2));
}

TEST(completely_empty_board_is_valid) { CHECK(valid(empty_board())); }

TEST(duplicate_in_a_row) {
    Rows rows = empty_board();
    rows[0] = "1.......1";
    CHECK(!valid(rows));
}

TEST(duplicate_in_a_column_across_different_boxes) {
    Rows rows = empty_board();
    rows[0] = "1........";
    rows[4] = "1........";
    CHECK(!valid(rows));
}

TEST(duplicate_inside_a_box_only) {
    // same box, but different row and different column
    Rows rows = empty_board();
    rows[0] = "1........";
    rows[1] = ".1.......";
    CHECK(!valid(rows));
}

TEST(same_digit_in_different_row_column_and_box_is_fine) {
    Rows rows = empty_board();
    rows[0] = "1........";
    rows[4] = "....1....";
    rows[8] = "........1";
    CHECK(valid(rows));
}

TEST(duplicate_in_the_last_box) {
    Rows rows = empty_board();
    rows[7] = ".......9.";
    rows[8] = "........9";
    CHECK(!valid(rows));
}

TEST(middle_box_duplicate) {
    Rows rows = empty_board();
    rows[3] = "...7.....";
    rows[5] = ".....7...";
    CHECK(!valid(rows));
}

TEST(a_solved_board_is_valid) {
    CHECK(valid(Rows{"534678912", "672195348", "198342567", "859761423",
                     "426853791", "713924856", "961537284", "287419635",
                     "345286179"}));
}
