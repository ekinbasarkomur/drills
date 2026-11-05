// 85. Maximal Rectangle · Hard · https://leetcode.com/problems/maximal-rectangle/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
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
        check_eq!(Solution::maximal_rectangle(vec![vec!['1', '0', '1', '0', '0'], vec!['1', '0', '1', '1', '1'], vec!['1', '1', '1', '1', '1'], vec!['1', '0', '0', '1', '0']]), 6);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::maximal_rectangle(vec![vec!['0']]), 0);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::maximal_rectangle(vec![vec!['1']]), 1);
    }
}
