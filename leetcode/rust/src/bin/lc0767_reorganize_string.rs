// 767. Reorganize String · Medium · https://leetcode.com/problems/reorganize-string/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn reorganize_string(s: String) -> String {
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
        let want: String = "aba".to_string();
        check_eq!(Solution::reorganize_string("aab".to_string()), want);
    }

    #[test]
    fn example_2() {
        let want: String = "".to_string();
        check_eq!(Solution::reorganize_string("aaab".to_string()), want);
    }
}
