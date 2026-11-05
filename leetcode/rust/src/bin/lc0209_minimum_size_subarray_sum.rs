// 209. Minimum Size Subarray Sum · Medium · https://leetcode.com/problems/minimum-size-subarray-sum/
// Plan: Aşama 0 · Sliding Window ve Prefix Sum
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
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
        check_eq!(Solution::min_sub_array_len(7, vec![2, 3, 1, 2, 4, 3]), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::min_sub_array_len(4, vec![1, 4, 4]), 1);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::min_sub_array_len(11, vec![1, 1, 1, 1, 1, 1, 1, 1]), 0);
    }
}
