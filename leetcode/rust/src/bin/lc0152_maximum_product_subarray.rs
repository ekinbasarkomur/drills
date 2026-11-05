// 152. Maximum Product Subarray · Medium · https://leetcode.com/problems/maximum-product-subarray/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
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
        check_eq!(Solution::max_product(vec![2, 3, -2, 4]), 6);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::max_product(vec![-2, 0, -1]), 0);
    }
}
