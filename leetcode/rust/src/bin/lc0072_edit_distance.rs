// 72. Edit Distance · Medium · https://leetcode.com/problems/edit-distance/
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
    pub fn min_distance(word1: String, word2: String) -> i32 {
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
        assert_eq!(Solution::min_distance("horse".to_string(), "ros".to_string()), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::min_distance("intention".to_string(), "execution".to_string()), 5);
    }
}
