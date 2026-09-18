// 104. Maximum Depth of Binary Tree
// https://leetcode.com/problems/maximum-depth-of-binary-tree/
//
// Problem: the number of nodes along the longest root-to-leaf path.
//          An empty tree has depth 0, a single node has depth 1.
// Note: LeetCode's Rust tree type is Option<Rc<RefCell<TreeNode>>>. Rc allows
//       more than one handle to a node, RefCell moves the borrow check to
//       runtime. To read a node: `node.borrow()`.
// Approach:
// Time O(?), space O(?)

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

// LeetCode's definition, verbatim.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode { val, left: None, right: None }
    }
}

type Link = Option<Rc<RefCell<TreeNode>>>;

struct Solution;

impl Solution {
    pub fn max_depth(root: Link) -> i32 {
        let _ = root;
        todo!()
    }
}

fn main() {
    let tree = build(&[Some(1), Some(2), Some(3), None, None, Some(4)]);
    println!("{}", Solution::max_depth(tree));
}

/// Level order, None marks a missing child.
fn build(values: &[Option<i32>]) -> Link {
    if values.is_empty() || values[0].is_none() {
        return None;
    }

    let root = Rc::new(RefCell::new(TreeNode::new(values[0].unwrap())));
    let mut queue = VecDeque::new();
    queue.push_back(Rc::clone(&root));

    let mut i = 1;
    while let Some(node) = queue.pop_front() {
        if i >= values.len() {
            break;
        }
        if let Some(v) = values[i] {
            let child = Rc::new(RefCell::new(TreeNode::new(v)));
            node.borrow_mut().left = Some(Rc::clone(&child));
            queue.push_back(child);
        }
        i += 1;

        if i >= values.len() {
            break;
        }
        if let Some(v) = values[i] {
            let child = Rc::new(RefCell::new(TreeNode::new(v)));
            node.borrow_mut().right = Some(Rc::clone(&child));
            queue.push_back(child);
        }
        i += 1;
    }
    root.into()
}

#[allow(dead_code)] // used once the tests compare whole trees
fn to_level_order(root: Link) -> Vec<Option<i32>> {
    let mut out = Vec::new();
    let Some(root) = root else { return out };

    let mut queue: VecDeque<Link> = VecDeque::new();
    queue.push_back(Some(root));

    while let Some(slot) = queue.pop_front() {
        match slot {
            None => out.push(None),
            Some(node) => {
                let node = node.borrow();
                out.push(Some(node.val));
                queue.push_back(node.left.clone());
                queue.push_back(node.right.clone());
            }
        }
    }
    while out.last() == Some(&None) {
        out.pop();
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn depth(values: &[Option<i32>]) -> i32 {
        Solution::max_depth(build(values))
    }

    const X: Option<i32> = None;
    fn n(v: i32) -> Option<i32> {
        Some(v)
    }

    #[test]
    fn example_1() {
        assert_eq!(depth(&[n(1), n(2), n(3), X, X, n(4)]), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(depth(&[]), 0);
    }

    #[test]
    fn single_node() {
        assert_eq!(depth(&[n(1)]), 1);
    }

    #[test]
    fn two_levels_full() {
        assert_eq!(depth(&[n(1), n(2), n(3)]), 2);
    }

    #[test]
    fn only_a_left_child() {
        assert_eq!(depth(&[n(1), n(2)]), 2);
    }

    #[test]
    fn only_a_right_child() {
        assert_eq!(depth(&[n(1), X, n(2)]), 2);
    }

    #[test]
    fn a_left_leaning_chain() {
        assert_eq!(depth(&[n(1), n(2), X, n(3), X, n(4)]), 4);
    }

    #[test]
    fn a_right_leaning_chain() {
        assert_eq!(depth(&[n(1), X, n(2), X, n(3), X, n(4)]), 4);
    }

    #[test]
    fn the_deep_side_is_on_the_right() {
        assert_eq!(depth(&[n(1), n(2), n(3), X, X, n(4), n(5), n(6)]), 4);
    }

    #[test]
    fn a_full_tree_of_three_levels() {
        assert_eq!(depth(&[n(1), n(2), n(3), n(4), n(5), n(6), n(7)]), 3);
    }

    #[test]
    fn largest_allowed_input() {
        // 100 nodes in a single chain, the constraint's ceiling.
        let mut values = Vec::new();
        for i in 0..100 {
            values.push(n(i));
            if i < 99 {
                values.push(X);
            }
        }
        assert_eq!(depth(&values), 100);
    }
}
