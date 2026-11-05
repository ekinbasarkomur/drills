// 19. Remove Nth Node From End of List · Medium · https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Plan: Aşama 0 · Linked List
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
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
        let want: Vec<i32> = vec![1, 2, 3, 5];
        check_eq!(list_to_vec(&Solution::remove_nth_from_end(build_list(&[1, 2, 3, 4, 5]), 2)), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![];
        check_eq!(list_to_vec(&Solution::remove_nth_from_end(build_list(&[1]), 1)), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![1];
        check_eq!(list_to_vec(&Solution::remove_nth_from_end(build_list(&[1, 2]), 1)), want);
    }
}
