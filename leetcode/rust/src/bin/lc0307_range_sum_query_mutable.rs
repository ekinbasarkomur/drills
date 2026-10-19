// 307. Range Sum Query - Mutable · Medium · https://leetcode.com/problems/range-sum-query-mutable/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct NumArray {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        todo!()
    }
    
    fn update(&self, index: i32, val: i32) {
        todo!()
    }
    
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        todo!()
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * obj.update(index, val);
 * let ret_2: i32 = obj.sum_range(left, right);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = NumArray::new(vec![1, 3, 5]);
        assert_eq!(obj.sum_range(0, 2), 9);
        obj.update(1, 2);
        assert_eq!(obj.sum_range(0, 2), 8);
    }
}
