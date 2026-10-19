// 703. Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/
// Plan: Aşama 0 · Heap & Priority Queue
//
// Problem: add() appends to the stream and returns the kth largest value seen
//          so far. Duplicates count separately: the 2nd largest of [1,2,3,3]
//          is 3.
// Note: you never need the whole stream -- only the k largest values, and of
//       those only the smallest is ever the answer. Rust's BinaryHeap is a
//       MAX-heap; std::cmp::Reverse turns it into a min-heap.
// Approach:
// Time O(?) per add, space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct KthLargest {
    // TODO: what does this need to hold?
}

impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let _ = (k, nums);
        todo!()
    }

    fn add(&mut self, val: i32) -> i32 {
        let _ = val;
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let mut s = KthLargest::new(3, vec![1, 2, 3, 3]);
    println!("{}", s.add(3));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut s = KthLargest::new(3, vec![1, 2, 3, 3]);
        assert_eq!(s.add(3), 3);
        assert_eq!(s.add(5), 3);
        assert_eq!(s.add(6), 3);
        assert_eq!(s.add(7), 5);
        assert_eq!(s.add(8), 6);
    }

    #[test]
    fn k_is_one_means_the_running_maximum() {
        let mut s = KthLargest::new(1, vec![]);
        assert_eq!(s.add(5), 5);
        assert_eq!(s.add(3), 5);
        assert_eq!(s.add(9), 9);
    }

    #[test]
    fn stream_starts_empty() {
        let mut s = KthLargest::new(2, vec![]);
        s.add(1);
        assert_eq!(s.add(2), 1);
        assert_eq!(s.add(3), 2);
    }

    #[test]
    fn initial_array_already_holds_k_values() {
        let mut s = KthLargest::new(3, vec![4, 5, 8, 2]);
        assert_eq!(s.add(3), 4);
        assert_eq!(s.add(5), 5);
        assert_eq!(s.add(10), 5);
        assert_eq!(s.add(9), 8);
    }

    #[test]
    fn duplicates_count_separately() {
        let mut s = KthLargest::new(2, vec![3, 3]);
        assert_eq!(s.add(3), 3);
        assert_eq!(s.add(4), 3);
    }

    #[test]
    fn everything_added_is_smaller() {
        let mut s = KthLargest::new(2, vec![10, 20, 30]);
        assert_eq!(s.add(1), 20);
        assert_eq!(s.add(2), 20);
    }

    #[test]
    fn negative_values() {
        let mut s = KthLargest::new(2, vec![-5, -3, -1]);
        assert_eq!(s.add(-4), -3);
        assert_eq!(s.add(0), -1);
    }

    #[test]
    fn all_values_equal() {
        let mut s = KthLargest::new(3, vec![7, 7, 7]);
        assert_eq!(s.add(7), 7);
        assert_eq!(s.add(8), 7);
    }

    #[test]
    fn value_range_extremes() {
        let mut s = KthLargest::new(2, vec![-1000, 1000]);
        assert_eq!(s.add(0), 0);
        assert_eq!(s.add(1000), 1000);
    }

    #[test]
    fn k_equals_the_stream_length() {
        let mut s = KthLargest::new(3, vec![1, 2]);
        assert_eq!(s.add(3), 1);
        assert_eq!(s.add(4), 2);
    }

    #[test]
    fn many_operations() {
        // 1000 values in, k = 1000: the answer is the running minimum
        // once the stream is long enough.
        let mut s = KthLargest::new(1000, vec![]);
        let mut last = 0;
        for i in (1..=1000).rev() {
            last = s.add(i);
        }
        assert_eq!(last, 1);
    }
}
