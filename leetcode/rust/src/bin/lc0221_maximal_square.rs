// 221. Maximal Square · Medium · https://leetcode.com/problems/maximal-square/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
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
        assert_eq!(Solution::maximal_square(vec![vec!['1', '0', '1', '0', '0'], vec!['1', '0', '1', '1', '1'], vec!['1', '1', '1', '1', '1'], vec!['1', '0', '0', '1', '0']]), 4);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::maximal_square(vec![vec!['0', '1'], vec!['1', '0']]), 1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::maximal_square(vec![vec!['0']]), 0);
    }
}
