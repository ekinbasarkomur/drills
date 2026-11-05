// 496. Next Greater Element I · Easy · https://leetcode.com/problems/next-greater-element-i/
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
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![-1, 3, -1];
        check_eq!(Solution::next_greater_element(vec![4, 1, 2], vec![1, 3, 4, 2]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![3, -1];
        check_eq!(Solution::next_greater_element(vec![2, 4], vec![1, 2, 3, 4]), want);
    }
}
