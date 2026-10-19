// 560. Subarray Sum Equals K · Medium · https://leetcode.com/problems/subarray-sum-equals-k/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
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
        assert_eq!(Solution::subarray_sum(vec![1, 1, 1], 2), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::subarray_sum(vec![1, 2, 3], 3), 2);
    }
}
