// 155. Min Stack
// https://leetcode.com/problems/min-stack/
// Plan: Aşama 0 · Stack
//
// Problem: a stack that also answers get_min() -- all four operations in O(1).
// Note: get_min in O(1) is the whole problem. Scanning for the minimum is O(n),
//       and a single "current min" field cannot survive a pop that removes it,
//       because you no longer know what the minimum was before.
// Approach:
// Time O(?) per operation, space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MinStack {
    // TODO: what does this need to hold?
}

#[allow(dead_code)] // every method is exercised by the tests once implemented
impl MinStack {
    fn new() -> Self {
        todo!()
    }

    fn push(&mut self, val: i32) {
        let _ = val;
        todo!()
    }

    fn pop(&mut self) {
        todo!()
    }

    fn top(&self) -> i32 {
        todo!()
    }

    fn get_min(&self) -> i32 {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    let mut s = MinStack::new();
    s.push(1);
    s.push(2);
    s.push(0);
    println!("{}", s.get_min());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut s = MinStack::new();
        s.push(1);
        s.push(2);
        s.push(0);
        assert_eq!(s.get_min(), 0);
        s.pop();
        assert_eq!(s.top(), 2);
        assert_eq!(s.get_min(), 1);
    }

    #[test]
    fn single_element() {
        let mut s = MinStack::new();
        s.push(5);
        assert_eq!(s.top(), 5);
        assert_eq!(s.get_min(), 5);
    }

    #[test]
    fn min_is_the_first_pushed() {
        let mut s = MinStack::new();
        for v in [1, 2, 3] {
            s.push(v);
        }
        assert_eq!(s.get_min(), 1);
        assert_eq!(s.top(), 3);
    }

    #[test]
    fn min_is_the_last_pushed() {
        let mut s = MinStack::new();
        for v in [3, 2, 1] {
            s.push(v);
        }
        assert_eq!(s.get_min(), 1);
    }

    #[test]
    fn popping_the_minimum_restores_the_previous_one() {
        let mut s = MinStack::new();
        s.push(5);
        s.push(1);
        assert_eq!(s.get_min(), 1);
        s.pop();
        assert_eq!(s.get_min(), 5);
    }

    #[test]
    fn duplicate_minimums() {
        // popping one copy of the minimum must not lose the other
        let mut s = MinStack::new();
        for v in [2, 1, 1] {
            s.push(v);
        }
        assert_eq!(s.get_min(), 1);
        s.pop();
        assert_eq!(s.get_min(), 1);
        s.pop();
        assert_eq!(s.get_min(), 2);
    }

    #[test]
    fn negative_values() {
        let mut s = MinStack::new();
        for v in [0, -3, 2] {
            s.push(v);
        }
        assert_eq!(s.get_min(), -3);
        s.pop();
        assert_eq!(s.get_min(), -3);
    }

    #[test]
    fn emptied_and_refilled() {
        let mut s = MinStack::new();
        s.push(1);
        s.pop();
        s.push(9);
        assert_eq!(s.top(), 9);
        assert_eq!(s.get_min(), 9);
    }

    #[test]
    fn interleaved_operations() {
        let mut s = MinStack::new();
        s.push(4);
        assert_eq!(s.get_min(), 4);
        s.push(7);
        assert_eq!(s.get_min(), 4);
        s.push(2);
        assert_eq!(s.get_min(), 2);
        s.pop();
        assert_eq!(s.get_min(), 4);
        s.push(1);
        assert_eq!(s.get_min(), 1);
        s.pop();
        s.pop();
        assert_eq!(s.top(), 4);
        assert_eq!(s.get_min(), 4);
    }

    #[test]
    fn value_range_extremes() {
        let mut s = MinStack::new();
        s.push(i32::MAX);
        s.push(i32::MIN);
        assert_eq!(s.get_min(), i32::MIN);
        s.pop();
        assert_eq!(s.get_min(), i32::MAX);
    }

    #[test]
    fn many_operations_stay_constant_time() {
        // 30_000 pushes then 30_000 pops, the constraint's ceiling.
        // An O(n) get_min will crawl here.
        let mut s = MinStack::new();
        for i in (1..=30_000).rev() {
            s.push(i);
        }
        for i in 1..=30_000 {
            assert_eq!(s.get_min(), i);
            s.pop();
        }
    }
}
