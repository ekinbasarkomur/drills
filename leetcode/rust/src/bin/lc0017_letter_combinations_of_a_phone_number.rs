// 17. Letter Combinations of a Phone Number · Medium · https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// Plan: Aşama 4 · Backtracking
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
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
        let want: Vec<String> = vec!["ad".to_string(), "ae".to_string(), "af".to_string(), "bd".to_string(), "be".to_string(), "bf".to_string(), "cd".to_string(), "ce".to_string(), "cf".to_string()];
        check_eq!(deep_sort(Solution::letter_combinations("23".to_string())), deep_sort(want));
    }

    #[test]
    fn example_2() {
        let want: Vec<String> = vec!["a".to_string(), "b".to_string(), "c".to_string()];
        check_eq!(deep_sort(Solution::letter_combinations("2".to_string())), deep_sort(want));
    }
}
