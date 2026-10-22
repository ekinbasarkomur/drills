// 66. Plus One · Easy · https://leetcode.com/problems/plus-one/
// Plan: Aşama 0 · Math
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![1, 2, 4];
        assert_eq!(Solution::plus_one(vec![1, 2, 3]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![4, 3, 2, 2];
        assert_eq!(Solution::plus_one(vec![4, 3, 2, 1]), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![1, 0];
        assert_eq!(Solution::plus_one(vec![9]), want);
    }
}
