// 153. Find Minimum in Rotated Sorted Array · Medium · https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Plan: Aşama 0 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::find_min(vec![3, 4, 5, 1, 2]), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::find_min(vec![4, 5, 6, 7, 0, 1, 2]), 0);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::find_min(vec![11, 13, 15, 17]), 11);
    }
}
