// 36. Valid Sudoku             https://leetcode.com/problems/valid-sudoku/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: a 9x9 board is valid if no row, no column and no 3x3 sub-box holds a
//          repeated digit. Empty cells are '.' and the board need not be
//          solvable, or even full.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        fn duplicate_exist(arr: Vec<char>) -> bool {
            let mut set: HashSet<char> = HashSet::new();

            for number in arr {
                if number == '.' {
                    continue;
                }

                match set.insert(number) {
                    true => continue,
                    false => return true,
                }
            }

            false
        }

        for i in 0..9 {
            let mut row: Vec<char> = vec![];
            let mut col: Vec<char> = vec![];
            let mut subbox: Vec<char> = vec![];

            for j in 0..9 {
                row.push(board[i][j]);
                col.push(board[j][i]);

                let row_num = (j / 3) + (3 * (i % 3));
                let col_num = (j % 3) + (3 * (i / 3));
                subbox.push(board[row_num][col_num]);
            }

            if duplicate_exist(row) {
                return false;
            }

            if duplicate_exist(col) {
                return false;
            }

            if duplicate_exist(subbox) {
                return false;
            }
        }

        true
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let board: Vec<Vec<char>> = [
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
    .iter()
    .map(|row| row.chars().collect())
    .collect();

    println!("{}", Solution::is_valid_sudoku(board));
}

#[cfg(test)]
mod tests {
    use super::*;

    // Boards are written as nine 9-character strings for readability.
    fn board(rows: [&str; 9]) -> Vec<Vec<char>> {
        assert!(rows.iter().all(|r| r.len() == 9));
        rows.iter().map(|row| row.chars().collect()).collect()
    }

    fn valid(rows: [&str; 9]) -> bool {
        Solution::is_valid_sudoku(board(rows))
    }

    const EMPTY: [&str; 9] = ["........."; 9];

    const EXAMPLE_1: [&str; 9] = [
        "12..3....",
        "4..5.....",
        ".98.....3",
        "5...6...4",
        "...8.3..5",
        "7...2...6",
        "......2..",
        "...419..8",
        "....8..79",
    ];

    const EXAMPLE_2: [&str; 9] = [
        "12..3....",
        "4..5.....",
        ".91.....3",
        "5...6...4",
        "...8.3..5",
        "7...2...6",
        "......2..",
        "...419..8",
        "....8..79",
    ];

    #[test]
    fn example_1() {
        assert!(valid(EXAMPLE_1));
    }

    #[test]
    fn example_2() {
        // two 1's in the top-left 3x3 sub-box
        assert!(!valid(EXAMPLE_2));
    }

    #[test]
    fn completely_empty_board_is_valid() {
        assert!(valid(EMPTY));
    }

    #[test]
    fn duplicate_in_a_row() {
        let mut rows = EMPTY;
        rows[0] = "1.......1";
        assert!(!valid(rows));
    }

    #[test]
    fn duplicate_in_a_column_across_different_boxes() {
        let mut rows = EMPTY;
        rows[0] = "1........";
        rows[4] = "1........";
        assert!(!valid(rows));
    }

    #[test]
    fn duplicate_inside_a_box_only() {
        // same box, but different row and different column
        let mut rows = EMPTY;
        rows[0] = "1........";
        rows[1] = ".1.......";
        assert!(!valid(rows));
    }

    #[test]
    fn same_digit_in_different_row_column_and_box_is_fine() {
        let mut rows = EMPTY;
        rows[0] = "1........";
        rows[4] = "....1....";
        rows[8] = "........1";
        assert!(valid(rows));
    }

    #[test]
    fn duplicate_in_the_last_box() {
        let mut rows = EMPTY;
        rows[7] = ".......9.";
        rows[8] = "........9";
        assert!(!valid(rows));
    }

    #[test]
    fn middle_box_duplicate() {
        let mut rows = EMPTY;
        rows[3] = "...7.....";
        rows[5] = ".....7...";
        assert!(!valid(rows));
    }

    #[test]
    fn a_solved_board_is_valid() {
        assert!(valid([
            "534678912",
            "672195348",
            "198342567",
            "859761423",
            "426853791",
            "713924856",
            "961537284",
            "287419635",
            "345286179",
        ]));
    }
}
