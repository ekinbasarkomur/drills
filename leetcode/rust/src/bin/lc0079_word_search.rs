// 79. Word Search · Medium · https://leetcode.com/problems/word-search/
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
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
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
        assert_eq!(Solution::exist(vec![vec!['A', 'B', 'C', 'E'], vec!['S', 'F', 'C', 'S'], vec!['A', 'D', 'E', 'E']], "ABCCED".to_string()), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::exist(vec![vec!['A', 'B', 'C', 'E'], vec!['S', 'F', 'C', 'S'], vec!['A', 'D', 'E', 'E']], "SEE".to_string()), true);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::exist(vec![vec!['A', 'B', 'C', 'E'], vec!['S', 'F', 'C', 'S'], vec!['A', 'D', 'E', 'E']], "ABCB".to_string()), false);
    }
}
