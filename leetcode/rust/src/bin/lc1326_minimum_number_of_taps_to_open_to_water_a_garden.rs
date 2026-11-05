// 1326. Minimum Number of Taps to Open to Water a Garden · Hard · https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
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
        check_eq!(Solution::min_taps(5, vec![3, 4, 1, 1, 0, 0]), 1);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::min_taps(3, vec![0, 0, 0, 0]), -1);
    }
}
