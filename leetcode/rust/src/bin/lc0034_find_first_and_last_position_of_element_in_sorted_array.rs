// 34. Find First and Last Position of Element in Sorted Array · Medium · https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
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
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
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
        let want: Vec<i32> = vec![3, 4];
        assert_eq!(Solution::search_range(vec![5, 7, 7, 8, 8, 10], 8), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![-1, -1];
        assert_eq!(Solution::search_range(vec![5, 7, 7, 8, 8, 10], 6), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![-1, -1];
        assert_eq!(Solution::search_range(vec![], 0), want);
    }
}
