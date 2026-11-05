// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/
// Plan: Aşama 0 · Greedy
//
// Problem: the largest sum any contiguous non-empty stretch of nums can
//          reach. Every value may be negative.
// Note: At each position you only ever choose between extending the run so
//       far and starting fresh -- whichever sum is larger.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let _ = (nums,);
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::max_sub_array(vec![2, -3, 4, -2, 2, 1, -1, 4]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn max_sub_array(nums: &[i32]) -> i32 {
        Solution::max_sub_array(nums.to_vec())
    }

    #[test]
    fn example_1() {
        check_eq!(max_sub_array(&[2, -3, 4, -2, 2, 1, -1, 4]), 8);
    }

    #[test]
    fn example_2() {
        // the subarray must be non-empty, so 0 is not an answer
        check_eq!(max_sub_array(&[-1]), -1);
    }

    #[test]
    fn single_positive() {
        check_eq!(max_sub_array(&[1]), 1);
    }

    #[test]
    fn single_zero() {
        check_eq!(max_sub_array(&[0]), 0);
    }

    #[test]
    fn the_classic_leetcode_case() {
        check_eq!(max_sub_array(&[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
    }

    #[test]
    fn every_value_negative() {
        // take the least bad one
        check_eq!(max_sub_array(&[-1, -2, -3]), -1);
    }

    #[test]
    fn a_dip_worth_crossing() {
        check_eq!(max_sub_array(&[5, 4, -1, 7, 8]), 23);
    }

    #[test]
    fn alternating_signs() {
        check_eq!(max_sub_array(&[1, -1, 1, -1, 1]), 1);
    }

    #[test]
    fn value_range_low() {
        check_eq!(max_sub_array(&[-10000]), -10000);
    }

    #[test]
    fn value_range_high() {
        check_eq!(max_sub_array(&[10000]), 10000);
    }

    #[test]
    fn largest_allowed_input() {
        // 100_000 values alternating +10_000 and -9_999, so each pair nets +1
        // and the best subarray is the whole array.
        // An O(n^2) solution will hang here rather than fail.
        let nums: Vec<i32> = (0..100_000)
            .map(|i| if i % 2 == 0 { 10_000 } else { -9_999 })
            .collect();
        check_eq!(max_sub_array(&nums), 59999);
    }
}
