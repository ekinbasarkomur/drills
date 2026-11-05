// 212. Word Search II · Hard · https://leetcode.com/problems/word-search-ii/
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
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
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
        let want: Vec<String> = vec!["eat".to_string(), "oath".to_string()];
        check_eq!(Solution::find_words(vec![vec!['o', 'a', 'a', 'n'], vec!['e', 't', 'a', 'e'], vec!['i', 'h', 'k', 'r'], vec!['i', 'f', 'l', 'v']], vec!["oath".to_string(), "pea".to_string(), "eat".to_string(), "rain".to_string()]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<String> = vec![];
        check_eq!(Solution::find_words(vec![vec!['a', 'b'], vec!['c', 'd']], vec!["abcb".to_string()]), want);
    }
}
