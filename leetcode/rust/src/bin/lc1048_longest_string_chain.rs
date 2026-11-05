// 1048. Longest String Chain · Medium · https://leetcode.com/problems/longest-string-chain/
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
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
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
        check_eq!(Solution::longest_str_chain(vec!["a".to_string(), "b".to_string(), "ba".to_string(), "bca".to_string(), "bda".to_string(), "bdca".to_string()]), 4);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::longest_str_chain(vec!["xbc".to_string(), "pcxbcf".to_string(), "xb".to_string(), "cxbc".to_string(), "pcxbc".to_string()]), 5);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::longest_str_chain(vec!["abcd".to_string(), "dbqca".to_string()]), 1);
    }
}
