// 23. Merge k Sorted Lists · Hard · https://leetcode.com/problems/merge-k-sorted-lists/
// Plan: Aşama 2 · Data Stream ve Heap
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
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
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
        let want: Vec<i32> = vec![1, 1, 2, 3, 4, 4, 5, 6];
        assert_eq!(list_to_vec(&Solution::merge_k_lists(vec![build_list(&[1, 4, 5]), build_list(&[1, 3, 4]), build_list(&[2, 6])])), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![];
        assert_eq!(list_to_vec(&Solution::merge_k_lists(vec![])), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![];
        assert_eq!(list_to_vec(&Solution::merge_k_lists(vec![build_list(&[])])), want);
    }
}
