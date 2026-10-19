// 43. Multiply Strings · Medium · https://leetcode.com/problems/multiply-strings/
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
    pub fn multiply(num1: String, num2: String) -> String {
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
        let want: String = "6".to_string();
        assert_eq!(Solution::multiply("2".to_string(), "3".to_string()), want);
    }

    #[test]
    fn example_2() {
        let want: String = "56088".to_string();
        assert_eq!(Solution::multiply("123".to_string(), "456".to_string()), want);
    }
}
