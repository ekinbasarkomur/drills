// 1319. Number of Operations to Make Network Connected · Medium · https://leetcode.com/problems/number-of-operations-to-make-network-connected/
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
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
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
        check_eq!(Solution::make_connected(4, vec![vec![0, 1], vec![0, 2], vec![1, 2]]), 1);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::make_connected(6, vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 2], vec![1, 3]]), 2);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::make_connected(6, vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 2]]), -1);
    }
}
