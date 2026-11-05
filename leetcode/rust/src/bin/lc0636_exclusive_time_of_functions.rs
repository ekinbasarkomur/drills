// 636. Exclusive Time of Functions · Medium · https://leetcode.com/problems/exclusive-time-of-functions/
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
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![3, 4];
        check_eq!(Solution::exclusive_time(2, vec!["0:start:0".to_string(), "1:start:2".to_string(), "1:end:5".to_string(), "0:end:6".to_string()]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![8];
        check_eq!(Solution::exclusive_time(1, vec!["0:start:0".to_string(), "0:start:2".to_string(), "0:end:5".to_string(), "0:start:6".to_string(), "0:end:6".to_string(), "0:end:7".to_string()]), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![7, 1];
        check_eq!(Solution::exclusive_time(2, vec!["0:start:0".to_string(), "0:start:2".to_string(), "0:end:5".to_string(), "1:start:6".to_string(), "1:end:6".to_string(), "0:end:7".to_string()]), want);
    }
}
