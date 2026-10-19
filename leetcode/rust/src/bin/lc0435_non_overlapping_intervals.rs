// 435. Non-overlapping Intervals · Medium · https://leetcode.com/problems/non-overlapping-intervals/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
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
        assert_eq!(Solution::erase_overlap_intervals(vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 3]]), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::erase_overlap_intervals(vec![vec![1, 2], vec![1, 2], vec![1, 2]]), 2);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::erase_overlap_intervals(vec![vec![1, 2], vec![2, 3]]), 0);
    }
}
