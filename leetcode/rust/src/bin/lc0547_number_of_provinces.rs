// 547. Number of Provinces · Medium · https://leetcode.com/problems/number-of-provinces/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
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
        check_eq!(Solution::find_circle_num(vec![vec![1, 1, 0], vec![1, 1, 0], vec![0, 0, 1]]), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::find_circle_num(vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]]), 3);
    }
}
