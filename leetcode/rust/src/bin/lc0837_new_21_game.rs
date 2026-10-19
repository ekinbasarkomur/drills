// 837. New 21 Game · Medium · https://leetcode.com/problems/new-21-game/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        assert!(approx_eq(Solution::new21_game(10, 1, 10), 1.0));
    }

    #[test]
    fn example_2() {
        assert!(approx_eq(Solution::new21_game(6, 1, 10), 0.6));
    }

    #[test]
    fn example_3() {
        assert!(approx_eq(Solution::new21_game(21, 17, 10), 0.73278));
    }
}
