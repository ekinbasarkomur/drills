// 100. Same Tree · Easy · https://leetcode.com/problems/same-tree/
// Plan: Aşama 0 · Trees
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
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
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
        check_eq!(Solution::is_same_tree(build_tree(&[Some(1), Some(2), Some(3)]), build_tree(&[Some(1), Some(2), Some(3)])), true);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::is_same_tree(build_tree(&[Some(1), Some(2)]), build_tree(&[Some(1), None, Some(2)])), false);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::is_same_tree(build_tree(&[Some(1), Some(2), Some(1)]), build_tree(&[Some(1), Some(1), Some(2)])), false);
    }
}
