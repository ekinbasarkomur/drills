// 399. Evaluate Division · Medium · https://leetcode.com/problems/evaluate-division/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn calc_equation(equations: Vec<Vec<String>>, values: Vec<f64>, queries: Vec<Vec<String>>) -> Vec<f64> {
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
        check!(approx_eq_vec(&Solution::calc_equation(vec![vec!["a".to_string(), "b".to_string()], vec!["b".to_string(), "c".to_string()]], vec![2.0, 3.0], vec![vec!["a".to_string(), "c".to_string()], vec!["b".to_string(), "a".to_string()], vec!["a".to_string(), "e".to_string()], vec!["a".to_string(), "a".to_string()], vec!["x".to_string(), "x".to_string()]]), &vec![6.0, 0.5, -1.0, 1.0, -1.0]));
    }

    #[test]
    fn example_2() {
        check!(approx_eq_vec(&Solution::calc_equation(vec![vec!["a".to_string(), "b".to_string()], vec!["b".to_string(), "c".to_string()], vec!["bc".to_string(), "cd".to_string()]], vec![1.5, 2.5, 5.0], vec![vec!["a".to_string(), "c".to_string()], vec!["c".to_string(), "b".to_string()], vec!["bc".to_string(), "cd".to_string()], vec!["cd".to_string(), "bc".to_string()]]), &vec![3.75, 0.4, 5.0, 0.2]));
    }

    #[test]
    fn example_3() {
        check!(approx_eq_vec(&Solution::calc_equation(vec![vec!["a".to_string(), "b".to_string()]], vec![0.5], vec![vec!["a".to_string(), "b".to_string()], vec!["b".to_string(), "a".to_string()], vec!["a".to_string(), "c".to_string()], vec!["x".to_string(), "y".to_string()]]), &vec![0.5, 2.0, -1.0, -1.0]));
    }
}
