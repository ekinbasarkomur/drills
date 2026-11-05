// 393. UTF-8 Validation · Medium · https://leetcode.com/problems/utf-8-validation/
// Plan: Aşama 1 · Bit Manipulation
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn valid_utf8(data: Vec<i32>) -> bool {
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
        check_eq!(Solution::valid_utf8(vec![197, 130, 1]), true);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::valid_utf8(vec![235, 140, 4]), false);
    }
}
