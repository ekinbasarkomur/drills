// 502. IPO · Hard · https://leetcode.com/problems/ipo/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn find_maximized_capital(k: i32, w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::find_maximized_capital(2, 0, vec![1, 2, 3], vec![0, 1, 1]), 4);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::find_maximized_capital(3, 0, vec![1, 2, 3], vec![0, 1, 2]), 6);
    }
}
