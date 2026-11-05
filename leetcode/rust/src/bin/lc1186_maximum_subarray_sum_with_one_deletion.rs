// 1186. Maximum Subarray Sum with One Deletion · Medium · https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
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
    pub fn maximum_sum(arr: Vec<i32>) -> i32 {
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
        check_eq!(Solution::maximum_sum(vec![1, -2, 0, 3]), 4);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::maximum_sum(vec![1, -2, -2, 3]), 3);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::maximum_sum(vec![-1, -1, -1, -1]), -1);
    }
}
