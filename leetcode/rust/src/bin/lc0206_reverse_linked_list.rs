// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
// Plan: Aşama 0 · Linked List
//
// Problem: reverse a singly linked list and return the new head.
// Note: Rust models a linked list as Option<Box<ListNode>> -- Option because a
//       node may or may not have a next, Box because a struct cannot contain
//       itself by value. `.take()` is how you pull a node out of an Option and
//       leave None behind, which is exactly the move this problem needs.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let list = build(&[0, 1, 2, 3]);
    println!("{:?}", to_vec(Solution::reverse_list(list)));
}

// Helpers shared by main and the tests.
fn build(values: &[i32]) -> Option<Box<ListNode>> {
    let mut head = None;
    for &v in values.iter().rev() {
        let mut node = Box::new(ListNode::new(v));
        node.next = head;
        head = Some(node);
    }
    head
}

fn to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut out = Vec::new();
    while let Some(node) = head {
        out.push(node.val);
        head = node.next;
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    fn reversed(values: &[i32]) -> Vec<i32> {
        to_vec(Solution::reverse_list(build(values)))
    }

    #[test]
    fn example_1() {
        assert_eq!(reversed(&[0, 1, 2, 3]), vec![3, 2, 1, 0]);
    }

    #[test]
    fn example_2() {
        assert_eq!(reversed(&[]), vec![]);
    }

    #[test]
    fn single_node() {
        assert_eq!(reversed(&[7]), vec![7]);
    }

    #[test]
    fn two_nodes() {
        assert_eq!(reversed(&[1, 2]), vec![2, 1]);
    }

    #[test]
    fn repeated_values() {
        assert_eq!(reversed(&[5, 5, 5]), vec![5, 5, 5]);
    }

    #[test]
    fn negative_values() {
        assert_eq!(reversed(&[-1, -2, -3]), vec![-3, -2, -1]);
    }

    #[test]
    fn value_range_extremes() {
        assert_eq!(reversed(&[-1000, 0, 1000]), vec![1000, 0, -1000]);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 nodes, the constraint's ceiling.
        let values: Vec<i32> = (0..1000).collect();
        let expected: Vec<i32> = (0..1000).rev().collect();
        assert_eq!(reversed(&values), expected);
    }
}
