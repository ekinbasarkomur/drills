// 2085. Count Common Words With One Occurrence · Easy · https://leetcode.com/problems/count-common-words-with-one-occurrence/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn count_words(words1: Vec<String>, words2: Vec<String>) -> i32 {
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
        assert_eq!(Solution::count_words(vec!["leetcode".to_string(), "is".to_string(), "amazing".to_string(), "as".to_string(), "is".to_string()], vec!["amazing".to_string(), "leetcode".to_string(), "is".to_string()]), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::count_words(vec!["b".to_string(), "bb".to_string(), "bbb".to_string()], vec!["a".to_string(), "aa".to_string(), "aaa".to_string()]), 0);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::count_words(vec!["a".to_string(), "ab".to_string()], vec!["a".to_string(), "a".to_string(), "a".to_string(), "ab".to_string()]), 1);
    }
}
