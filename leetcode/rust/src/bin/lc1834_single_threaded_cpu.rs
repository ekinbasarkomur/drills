// 1834. Single-Threaded CPU · Medium · https://leetcode.com/problems/single-threaded-cpu/
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
    pub fn get_order(tasks: Vec<Vec<i32>>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![0, 2, 3, 1];
        check_eq!(Solution::get_order(vec![vec![1, 2], vec![2, 4], vec![3, 2], vec![4, 1]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![4, 3, 2, 0, 1];
        check_eq!(Solution::get_order(vec![vec![7, 10], vec![7, 12], vec![7, 5], vec![7, 4], vec![7, 2]]), want);
    }
}
