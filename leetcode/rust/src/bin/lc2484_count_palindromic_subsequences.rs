// 2484. Count Palindromic Subsequences · Hard · https://leetcode.com/problems/count-palindromic-subsequences/
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
    pub fn count_palindromes(s: String) -> i32 {
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
        check_eq!(Solution::count_palindromes("103301".to_string()), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::count_palindromes("0000000".to_string()), 21);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::count_palindromes("9999900000".to_string()), 2);
    }
}
