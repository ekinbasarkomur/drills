// 94. Binary Tree Inorder Traversal · Easy · https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![1, 3, 2];
        assert_eq!(Solution::inorder_traversal(build_tree(&[Some(1), None, Some(2), Some(3)])), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![4, 2, 6, 5, 7, 1, 3, 9, 8];
        assert_eq!(Solution::inorder_traversal(build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5), None, Some(8), None, None, Some(6), Some(7), Some(9)])), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![];
        assert_eq!(Solution::inorder_traversal(build_tree(&[])), want);
    }

    #[test]
    fn example_4() {
        let want: Vec<i32> = vec![1];
        assert_eq!(Solution::inorder_traversal(build_tree(&[Some(1)])), want);
    }
}
