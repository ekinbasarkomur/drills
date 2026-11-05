// 1514. Path with Maximum Probability · Medium · https://leetcode.com/problems/path-with-maximum-probability/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn max_probability(n: i32, edges: Vec<Vec<i32>>, succ_prob: Vec<f64>, start_node: i32, end_node: i32) -> f64 {
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
        check!(approx_eq(Solution::max_probability(3, vec![vec![0, 1], vec![1, 2], vec![0, 2]], vec![0.5, 0.5, 0.2], 0, 2), 0.25));
    }

    #[test]
    fn example_2() {
        check!(approx_eq(Solution::max_probability(3, vec![vec![0, 1], vec![1, 2], vec![0, 2]], vec![0.5, 0.5, 0.3], 0, 2), 0.3));
    }

    #[test]
    fn example_3() {
        check!(approx_eq(Solution::max_probability(3, vec![vec![0, 1]], vec![0.5], 0, 2), 0.0));
    }
}
