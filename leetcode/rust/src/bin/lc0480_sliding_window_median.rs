// 480. Sliding Window Median · Hard · https://leetcode.com/problems/sliding-window-median/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn median_sliding_window(nums: Vec<i32>, k: i32) -> Vec<f64> {
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
        check!(approx_eq_vec(&Solution::median_sliding_window(vec![1, 3, -1, -3, 5, 3, 6, 7], 3), &vec![1.0, -1.0, -1.0, 3.0, 5.0, 6.0]));
    }

    #[test]
    fn example_2() {
        check!(approx_eq_vec(&Solution::median_sliding_window(vec![1, 2, 3, 4, 2, 3, 1, 4, 2], 3), &vec![2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]));
    }
}
