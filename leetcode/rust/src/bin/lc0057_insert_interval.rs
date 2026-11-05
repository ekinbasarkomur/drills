// 57. Insert Interval · Medium · https://leetcode.com/problems/insert-interval/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
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
        let want: Vec<Vec<i32>> = vec![vec![1, 5], vec![6, 9]];
        check_eq!(Solution::insert(vec![vec![1, 3], vec![6, 9]], vec![2, 5]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<i32>> = vec![vec![1, 2], vec![3, 10], vec![12, 16]];
        check_eq!(Solution::insert(vec![vec![1, 2], vec![3, 5], vec![6, 7], vec![8, 10], vec![12, 16]], vec![4, 8]), want);
    }
}
