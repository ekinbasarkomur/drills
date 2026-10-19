// 191. Number of 1 Bits · Easy · https://leetcode.com/problems/number-of-1-bits/
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
    pub fn hamming_weight(n: i32) -> i32 {
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
        assert_eq!(Solution::hamming_weight(11), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::hamming_weight(128), 1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::hamming_weight(2147483645), 30);
    }
}
