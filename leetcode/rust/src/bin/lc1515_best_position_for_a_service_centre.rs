// 1515. Best Position for a Service Centre · Hard · https://leetcode.com/problems/best-position-for-a-service-centre/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn get_min_dist_sum(positions: Vec<Vec<i32>>) -> f64 {
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
        check!(approx_eq(Solution::get_min_dist_sum(vec![vec![0, 1], vec![1, 0], vec![1, 2], vec![2, 1]]), 4.0));
    }

    #[test]
    fn example_2() {
        check!(approx_eq(Solution::get_min_dist_sum(vec![vec![1, 1], vec![3, 3]]), 2.82843));
    }
}
