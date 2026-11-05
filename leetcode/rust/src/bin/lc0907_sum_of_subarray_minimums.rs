// 907. Sum of Subarray Minimums · Medium · https://leetcode.com/problems/sum-of-subarray-minimums/
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
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
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
        check_eq!(Solution::sum_subarray_mins(vec![3, 1, 2, 4]), 17);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::sum_subarray_mins(vec![50]), 444);
    }
}
