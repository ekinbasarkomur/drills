// 4. Median of Two Sorted Arrays · Hard · https://leetcode.com/problems/median-of-two-sorted-arrays/
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
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
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
        check!(approx_eq(Solution::find_median_sorted_arrays(vec![1, 3], vec![2]), 2.0));
    }

    #[test]
    fn example_2() {
        check!(approx_eq(Solution::find_median_sorted_arrays(vec![1, 2], vec![3, 4]), 2.5));
    }
}
