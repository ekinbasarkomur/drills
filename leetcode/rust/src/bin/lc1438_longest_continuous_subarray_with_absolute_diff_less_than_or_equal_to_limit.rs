// 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit · Medium · https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
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
        check_eq!(Solution::longest_subarray(vec![8, 2, 4, 7], 4), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::longest_subarray(vec![10, 1, 2, 4, 7, 2], 5), 4);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::longest_subarray(vec![4, 2, 2, 2, 4, 4, 2, 2], 0), 3);
    }
}
