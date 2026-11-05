// 410. Split Array Largest Sum · Hard · https://leetcode.com/problems/split-array-largest-sum/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn split_array(nums: Vec<i32>, k: i32) -> i32 {
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
        check_eq!(Solution::split_array(vec![7, 2, 5, 10, 8], 2), 18);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::split_array(vec![1, 2, 3, 4, 5], 2), 9);
    }
}
