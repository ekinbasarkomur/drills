// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/
// Plan: Aşama 0 · Two Pointers
//
// Problem: pick two bars; the container they form holds
//          (distance between them) * (the shorter of the two). Return the most
//          water any pair can hold.
// Note: The taller bar never sets the height -- the shorter one does, so a
//       wide pair of short bars can beat a narrow pair of tall ones.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let _ = (height,);
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::max_area(vec![1, 7, 2, 5, 4, 7, 3, 6]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn max_area(height: &[i32]) -> i32 {
        Solution::max_area(height.to_vec())
    }

    #[test]
    fn example_1() {
        check_eq!(max_area(&[1, 7, 2, 5, 4, 7, 3, 6]), 36);
    }

    #[test]
    fn example_2() {
        check_eq!(max_area(&[2, 2, 2]), 4);
    }

    #[test]
    fn shortest_possible_input() {
        check_eq!(max_area(&[1, 1]), 1);
    }

    #[test]
    fn two_zero_bars_hold_nothing() {
        check_eq!(max_area(&[0, 0]), 0);
    }

    #[test]
    fn the_classic_leetcode_case() {
        check_eq!(max_area(&[1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
    }

    #[test]
    fn wide_beats_tall() {
        // the two 3s are 2 apart; nothing taller sits closer together
        check_eq!(max_area(&[3, 0, 3]), 6);
    }

    #[test]
    fn strictly_ascending() {
        check_eq!(max_area(&[1, 2, 3, 4, 5]), 6);
    }

    #[test]
    fn strictly_descending() {
        check_eq!(max_area(&[5, 4, 3, 2, 1]), 6);
    }

    #[test]
    fn one_zero_bar_kills_the_pair() {
        check_eq!(max_area(&[0, 10000]), 0);
    }

    #[test]
    fn value_range_extremes() {
        check_eq!(max_area(&[10000, 0, 0, 0, 10000]), 40000);
    }

    #[test]
    fn largest_allowed_input() {
        // 100_000 bars: 1 at both ends, 0 in between. The answer is the pair of
        // ends, worth 99_999. An O(n^2) solution will hang here rather than fail.
        let mut height = vec![0; 100_000];
        height[0] = 1;
        height[99_999] = 1;
        check_eq!(max_area(&height), 99999);
    }
}
