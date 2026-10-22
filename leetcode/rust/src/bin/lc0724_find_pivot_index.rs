// 724. Find Pivot Index · Easy · https://leetcode.com/problems/find-pivot-index/
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
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::pivot_index(vec![1, 7, 3, 6, 5, 6]), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::pivot_index(vec![1, 2, 3]), -1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::pivot_index(vec![2, 1, -1]), 0);
    }
}
