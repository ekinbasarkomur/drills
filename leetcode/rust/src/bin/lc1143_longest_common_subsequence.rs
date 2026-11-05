// 1143. Longest Common Subsequence · Medium · https://leetcode.com/problems/longest-common-subsequence/
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
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
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
        check_eq!(Solution::longest_common_subsequence("abcde".to_string(), "ace".to_string()), 3);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::longest_common_subsequence("abc".to_string(), "abc".to_string()), 3);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::longest_common_subsequence("abc".to_string(), "def".to_string()), 0);
    }
}
