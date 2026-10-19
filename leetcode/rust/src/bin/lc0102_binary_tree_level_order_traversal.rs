// 102. Binary Tree Level Order Traversal · Medium · https://leetcode.com/problems/binary-tree-level-order-traversal/
// Plan: Aşama 2 · Tree
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
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
        let want: Vec<Vec<i32>> = vec![vec![3], vec![9, 20], vec![15, 7]];
        assert_eq!(Solution::level_order(build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)])), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<i32>> = vec![vec![1]];
        assert_eq!(Solution::level_order(build_tree(&[Some(1)])), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<Vec<i32>> = vec![];
        assert_eq!(Solution::level_order(build_tree(&[])), want);
    }
}
