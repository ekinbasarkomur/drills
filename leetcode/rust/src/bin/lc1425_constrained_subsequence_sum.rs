// 1425. Constrained Subsequence Sum · Hard · https://leetcode.com/problems/constrained-subsequence-sum/
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
    pub fn constrained_subset_sum(nums: Vec<i32>, k: i32) -> i32 {
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
        check_eq!(Solution::constrained_subset_sum(vec![10, 2, -10, 5, 20], 2), 37);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::constrained_subset_sum(vec![-1, -2, -3], 1), -1);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::constrained_subset_sum(vec![10, -2, -10, -5, 20], 2), 23);
    }
}
