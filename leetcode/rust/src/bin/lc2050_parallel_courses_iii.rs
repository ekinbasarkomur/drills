// 2050. Parallel Courses III · Hard · https://leetcode.com/problems/parallel-courses-iii/
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
    pub fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
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
        check_eq!(Solution::minimum_time(3, vec![vec![1, 3], vec![2, 3]], vec![3, 2, 5]), 8);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::minimum_time(5, vec![vec![1, 5], vec![2, 5], vec![3, 5], vec![3, 4], vec![4, 5]], vec![1, 2, 3, 4, 5]), 12);
    }
}
