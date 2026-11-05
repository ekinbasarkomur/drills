// 230. Kth Smallest Element in a BST · Medium · https://leetcode.com/problems/kth-smallest-element-in-a-bst/
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
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
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
        check_eq!(Solution::kth_smallest(build_tree(&[Some(3), Some(1), Some(4), None, Some(2)]), 1), 1);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::kth_smallest(build_tree(&[Some(5), Some(3), Some(6), Some(2), Some(4), None, None, Some(1)]), 3), 3);
    }
}
