// 200. Number of Islands
// https://leetcode.com/problems/number-of-islands/
//
// Problem: count the connected groups of '1' cells in the grid. Cells join
//          horizontally and vertically only, never diagonally.
// Note: Once you reach a land cell, sink the whole island before moving on --
//       otherwise you count the same island once per cell.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let _ = (grid,);
        todo!()
    }
}

fn main() {
    let grid = ["01110", "01010", "11000", "00000"];
    println!("{}", Solution::num_islands(
        grid.iter().map(|r| r.chars().collect()).collect()));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn num_islands(grid: &[&str]) -> i32 {
        Solution::num_islands(grid.iter().map(|r| r.chars().collect()).collect())
    }

    #[test]
    fn example_1() {
        assert_eq!(num_islands(&["01110", "01010", "11000", "00000"]), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(num_islands(&["11001", "11001", "00100", "00011"]), 4);
    }

    #[test]
    fn all_water() {
        assert_eq!(num_islands(&["000", "000"]), 0);
    }

    #[test]
    fn all_land() {
        assert_eq!(num_islands(&["111", "111"]), 1);
    }

    #[test]
    fn single_cell_land() {
        assert_eq!(num_islands(&["1"]), 1);
    }

    #[test]
    fn single_cell_water() {
        assert_eq!(num_islands(&["0"]), 0);
    }

    #[test]
    fn one_row() {
        assert_eq!(num_islands(&["10101"]), 3);
    }

    #[test]
    fn one_column() {
        assert_eq!(num_islands(&["1", "0", "1", "1"]), 2);
    }

    #[test]
    fn diagonals_do_not_connect() {
        // touching corners is not adjacency
        assert_eq!(num_islands(&["10", "01"]), 2);
    }

    #[test]
    fn a_ring_of_land_around_water() {
        assert_eq!(num_islands(&["111", "101", "111"]), 1);
    }

    #[test]
    fn checkerboard() {
        assert_eq!(num_islands(&["101", "010", "101"]), 5);
    }

    #[test]
    fn largest_allowed_input() {
        // 100x100 checkerboard, the constraint's ceiling: 2500 single-cell
        // islands, none of them touching.
        let grid: Vec<String> = (0..100)
            .map(|r: usize| (0..100).map(|c| if (r + c) % 2 == 0 { '1' } else { '0' }).collect())
            .collect();
        let rows: Vec<&str> = grid.iter().map(|s| s.as_str()).collect();
        assert_eq!(num_islands(&rows), 2_500);
        assert_eq!(num_islands(&[]), 2500);
    }
}
