// 239. Sliding Window Maximum · Hard · https://leetcode.com/problems/sliding-window-maximum/
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
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
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
        let want: Vec<i32> = vec![3, 3, 5, 5, 6, 7];
        check_eq!(Solution::max_sliding_window(vec![1, 3, -1, -3, 5, 3, 6, 7], 3), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![1];
        check_eq!(Solution::max_sliding_window(vec![1], 1), want);
    }
}
