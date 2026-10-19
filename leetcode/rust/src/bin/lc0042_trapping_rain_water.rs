// 42. Trapping Rain Water      https://leetcode.com/problems/trapping-rain-water/
// Plan: Aşama 0 · Two Pointers
//
// Problem: each height[i] is a bar of width 1. How much water sits in the dips
//          once the rain stops?
// Key idea: water above bar i is min(tallest bar to its left,
//           tallest bar to its right) - height[i], never negative.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let _ = height;
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::trap(vec![0, 2, 0, 3, 1, 0, 1, 3, 2, 1]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn trap(height: &[i32]) -> i32 {
        Solution::trap(height.to_vec())
    }

    #[test]
    fn example_1() {
        assert_eq!(trap(&[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]), 9);
    }

    #[test]
    fn the_leetcode_example() {
        assert_eq!(trap(&[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6);
    }

    #[test]
    fn tall_wall_on_the_right() {
        assert_eq!(trap(&[4, 2, 0, 3, 2, 5]), 9);
    }

    // Nothing can be trapped in any of these.

    #[test]
    fn single_bar() {
        assert_eq!(trap(&[5]), 0);
    }

    #[test]
    fn two_bars() {
        assert_eq!(trap(&[3, 4]), 0);
    }

    #[test]
    fn strictly_ascending() {
        assert_eq!(trap(&[1, 2, 3, 4, 5]), 0);
    }

    #[test]
    fn strictly_descending() {
        assert_eq!(trap(&[5, 4, 3, 2, 1]), 0);
    }

    #[test]
    fn flat_ground() {
        assert_eq!(trap(&[3, 3, 3, 3]), 0);
    }

    #[test]
    fn all_zeros() {
        assert_eq!(trap(&[0, 0, 0]), 0);
    }

    #[test]
    fn a_peak_traps_nothing() {
        assert_eq!(trap(&[0, 100_000, 0]), 0);
    }

    // The real cases.

    #[test]
    fn one_simple_basin() {
        assert_eq!(trap(&[5, 0, 5]), 5);
    }

    #[test]
    fn two_basins_in_a_row() {
        assert_eq!(trap(&[2, 0, 2, 0, 2]), 4);
    }

    #[test]
    fn several_narrow_dips() {
        assert_eq!(trap(&[1, 0, 1, 0, 1, 0, 1]), 3);
    }

    #[test]
    fn value_range_extremes() {
        // one basin 100_000 deep -- the running total must not overflow an i32
        assert_eq!(trap(&[100_000, 0, 100_000]), 100_000);
    }

    #[test]
    fn largest_allowed_input() {
        // 20_000 bars alternating 100_000 and 0: 9_999 basins of 100_000 each.
        // An O(n^2) solution will hang here rather than fail.
        let mut height = Vec::new();
        for _ in 0..10_000 {
            height.push(100_000);
            height.push(0);
        }
        assert_eq!(trap(&height), 999_900_000);
    }
}
