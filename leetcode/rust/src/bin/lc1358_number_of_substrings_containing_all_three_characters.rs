// 1358. Number of Substrings Containing All Three Characters · Medium · https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
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
        assert_eq!(Solution::number_of_substrings("abcabc".to_string()), 10);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::number_of_substrings("aaacb".to_string()), 3);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::number_of_substrings("abc".to_string()), 1);
    }
}
