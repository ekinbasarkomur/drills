// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/
// Plan: Aşama 0 · Trees
//
// Problem: mirror the tree -- every node's left and right swap, all the way
//          down -- and return the root.
// Note: LeetCode's Rust tree type is Option<Rc<RefCell<TreeNode>>>. Rc allows
//       more than one handle to a node, RefCell moves the borrow check to
//       runtime so you can mutate through a shared handle. To touch a node:
//       `node.borrow_mut()`; to read: `node.borrow()`.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

type Link = Option<Rc<RefCell<TreeNode>>>;

impl Solution {
    pub fn invert_tree(root: Link) -> Link {
        root
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let tree = build(&[Some(1), Some(2), Some(3), Some(4), Some(5), Some(6), Some(7)]);
    println!("{:?}", to_level_order(Solution::invert_tree(tree)));
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

    fn inverted(values: &[Option<i32>]) -> Vec<Option<i32>> {
        to_level_order(Solution::invert_tree(build(values)))
    }

    // Shorthand so the test bodies read like the problem statement.
    const X: Option<i32> = None;
    fn n(v: i32) -> Option<i32> {
        Some(v)
    }

    #[test]
    fn example_1() {
        assert_eq!(
            inverted(&[n(1), n(2), n(3), n(4), n(5), n(6), n(7)]),
            vec![n(1), n(3), n(2), n(7), n(6), n(5), n(4)]
        );
    }

    #[test]
    fn example_2() {
        assert_eq!(inverted(&[n(3), n(2), n(1)]), vec![n(3), n(1), n(2)]);
    }

    #[test]
    fn example_3() {
        assert_eq!(inverted(&[]), vec![]);
    }

    #[test]
    fn single_node() {
        assert_eq!(inverted(&[n(1)]), vec![n(1)]);
    }

    #[test]
    fn only_a_left_child() {
        assert_eq!(inverted(&[n(1), n(2)]), vec![n(1), X, n(2)]);
    }

    #[test]
    fn only_a_right_child() {
        assert_eq!(inverted(&[n(1), X, n(2)]), vec![n(1), n(2)]);
    }

    #[test]
    fn a_left_leaning_chain_becomes_right_leaning() {
        assert_eq!(
            inverted(&[n(1), n(2), X, n(3)]),
            vec![n(1), X, n(2), X, n(3)]
        );
    }

    #[test]
    fn lopsided_tree() {
        assert_eq!(
            inverted(&[n(1), n(2), n(3), X, n(4)]),
            vec![n(1), n(3), n(2), X, X, n(4)]
        );
    }

    #[test]
    fn negative_values() {
        assert_eq!(inverted(&[n(-1), n(-2), n(-3)]), vec![n(-1), n(-3), n(-2)]);
    }

    #[test]
    fn inverting_twice_restores_the_original() {
        let original = [n(1), n(2), n(3), n(4), n(5), n(6), n(7)];
        let once = inverted(&original);
        assert_eq!(inverted(&once), original.to_vec());
    }

    #[test]
    fn a_symmetric_tree_is_unchanged() {
        assert_eq!(inverted(&[n(1), n(2), n(2)]), vec![n(1), n(2), n(2)]);
    }
}
