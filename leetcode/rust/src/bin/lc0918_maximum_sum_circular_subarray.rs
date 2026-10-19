// 918. Maximum Sum Circular Subarray · Medium · https://leetcode.com/problems/maximum-sum-circular-subarray/
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
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::max_subarray_sum_circular(vec![1, -2, 3, -2]), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::max_subarray_sum_circular(vec![5, -3, 5]), 10);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::max_subarray_sum_circular(vec![-3, -2, -3]), -2);
    }
}
