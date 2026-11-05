// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/
// Plan: Aşama 0 · Linked List
//
// Problem: splice two sorted lists into one sorted list, reusing the nodes.
// Note: the C++ "dummy head" trick is awkward here because Rust will not let
//       you hold a pointer into a structure you are also moving out of. The
//       two usual ways round it are recursion, or building the result with
//       `&mut Option<Box<ListNode>>` as a cursor.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let _ = list2;
        list1
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let merged = Solution::merge_two_lists(build(&[1, 2, 4]), build(&[1, 3, 5]));
    println!("{:?}", to_vec(merged));
}

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

    fn merged(a: &[i32], b: &[i32]) -> Vec<i32> {
        to_vec(Solution::merge_two_lists(build(a), build(b)))
    }

    #[test]
    fn example_1() {
        check_eq!(merged(&[1, 2, 4], &[1, 3, 5]), vec![1, 1, 2, 3, 4, 5]);
    }

    #[test]
    fn example_2() {
        check_eq!(merged(&[], &[1, 2]), vec![1, 2]);
    }

    #[test]
    fn example_3() {
        check_eq!(merged(&[], &[]), vec![]);
    }

    #[test]
    fn first_list_empty() {
        check_eq!(merged(&[], &[5]), vec![5]);
    }

    #[test]
    fn second_list_empty() {
        check_eq!(merged(&[5], &[]), vec![5]);
    }

    #[test]
    fn one_list_entirely_precedes_the_other() {
        check_eq!(merged(&[1, 2, 3], &[4, 5, 6]), vec![1, 2, 3, 4, 5, 6]);
        check_eq!(merged(&[4, 5, 6], &[1, 2, 3]), vec![1, 2, 3, 4, 5, 6]);
    }

    #[test]
    fn perfectly_interleaved() {
        check_eq!(merged(&[1, 3, 5], &[2, 4, 6]), vec![1, 2, 3, 4, 5, 6]);
    }

    #[test]
    fn all_values_equal() {
        check_eq!(merged(&[2, 2], &[2, 2]), vec![2, 2, 2, 2]);
    }

    #[test]
    fn very_different_lengths() {
        check_eq!(merged(&[1], &[2, 3, 4, 5]), vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn negative_values() {
        check_eq!(merged(&[-5, -1], &[-3, 0]), vec![-5, -3, -1, 0]);
    }

    #[test]
    fn value_range_extremes() {
        check_eq!(merged(&[-100, 100], &[0]), vec![-100, 0, 100]);
    }

    #[test]
    fn largest_allowed_input() {
        // 100 nodes each, the constraint's ceiling.
        let a: Vec<i32> = (0..100).map(|i| i * 2).collect();
        let b: Vec<i32> = (0..100).map(|i| i * 2 + 1).collect();
        let expected: Vec<i32> = (0..200).collect();
        check_eq!(merged(&a, &b), expected);
    }
}
