// 647. Palindromic Substrings · Medium · https://leetcode.com/problems/palindromic-substrings/
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
    pub fn count_substrings(s: String) -> i32 {
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
        check_eq!(Solution::count_substrings("abc".to_string()), 3);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::count_substrings("aaa".to_string()), 6);
    }
}
