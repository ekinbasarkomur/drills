// 718. Maximum Length of Repeated Subarray · Medium · https://leetcode.com/problems/maximum-length-of-repeated-subarray/
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
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
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
        check_eq!(Solution::find_length(vec![1, 2, 3, 2, 1], vec![3, 2, 1, 4, 7]), 3);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::find_length(vec![0, 0, 0, 0, 0], vec![0, 0, 0, 0, 0]), 5);
    }
}
