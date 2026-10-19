// 688. Knight Probability in Chessboard · Medium · https://leetcode.com/problems/knight-probability-in-chessboard/
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
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
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
        assert!(approx_eq(Solution::knight_probability(3, 2, 0, 0), 0.0625));
    }

    #[test]
    fn example_2() {
        assert!(approx_eq(Solution::knight_probability(1, 0, 0, 0), 1.0));
    }
}
