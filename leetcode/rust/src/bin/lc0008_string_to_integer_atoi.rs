// 8. String to Integer (atoi) · Medium · https://leetcode.com/problems/string-to-integer-atoi/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
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
        assert_eq!(Solution::my_atoi("42".to_string()), 42);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::my_atoi("   -042".to_string()), -42);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::my_atoi("1337c0d3".to_string()), 1337);
    }

    #[test]
    fn example_4() {
        assert_eq!(Solution::my_atoi("0-1".to_string()), 0);
    }

    #[test]
    fn example_5() {
        assert_eq!(Solution::my_atoi("words and 987".to_string()), 0);
    }
}
