// 1882. Process Tasks Using Servers · Medium · https://leetcode.com/problems/process-tasks-using-servers/
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
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![2, 2, 0, 2, 1, 2];
        assert_eq!(Solution::assign_tasks(vec![3, 3, 2], vec![1, 2, 3, 2, 1, 2]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![1, 4, 1, 4, 1, 3, 2];
        assert_eq!(Solution::assign_tasks(vec![5, 1, 4, 3, 2], vec![2, 1, 2, 4, 5, 2, 1]), want);
    }
}
