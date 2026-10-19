// 862. Shortest Subarray with Sum at Least K · Hard · https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
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
    pub fn shortest_subarray(nums: Vec<i32>, k: i32) -> i32 {
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
        assert_eq!(Solution::shortest_subarray(vec![1], 1), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::shortest_subarray(vec![1, 2], 4), -1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::shortest_subarray(vec![2, -1, 2], 3), 3);
    }
}
