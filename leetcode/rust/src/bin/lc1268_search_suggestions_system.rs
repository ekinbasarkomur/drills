// 1268. Search Suggestions System · Medium · https://leetcode.com/problems/search-suggestions-system/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn suggested_products(products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
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
        let want: Vec<Vec<String>> = vec![vec!["mobile".to_string(), "moneypot".to_string(), "monitor".to_string()], vec!["mobile".to_string(), "moneypot".to_string(), "monitor".to_string()], vec!["mouse".to_string(), "mousepad".to_string()], vec!["mouse".to_string(), "mousepad".to_string()], vec!["mouse".to_string(), "mousepad".to_string()]];
        assert_eq!(Solution::suggested_products(vec!["mobile".to_string(), "mouse".to_string(), "moneypot".to_string(), "monitor".to_string(), "mousepad".to_string()], "mouse".to_string()), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<String>> = vec![vec!["havana".to_string()], vec!["havana".to_string()], vec!["havana".to_string()], vec!["havana".to_string()], vec!["havana".to_string()], vec!["havana".to_string()]];
        assert_eq!(Solution::suggested_products(vec!["havana".to_string()], "havana".to_string()), want);
    }
}
