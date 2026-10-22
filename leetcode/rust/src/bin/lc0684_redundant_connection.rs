// 684. Redundant Connection · Medium · https://leetcode.com/problems/redundant-connection/
// Plan: Aşama 0 · Graphs
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![2, 3];
        assert_eq!(Solution::find_redundant_connection(vec![vec![1, 2], vec![1, 3], vec![2, 3]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![1, 4];
        assert_eq!(Solution::find_redundant_connection(vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 4], vec![1, 5]]), want);
    }
}
