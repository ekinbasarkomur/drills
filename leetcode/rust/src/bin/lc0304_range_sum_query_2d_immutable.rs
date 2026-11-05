// 304. Range Sum Query 2D - Immutable · Medium · https://leetcode.com/problems/range-sum-query-2d-immutable/
// Plan: Aşama 1 · Prefix Sum ve Sliding Window
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct NumMatrix {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumMatrix {

    fn new(matrix: Vec<Vec<i32>>) -> Self {
        todo!()
    }
    
    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        todo!()
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj = NumMatrix::new(matrix);
 * let ret_1: i32 = obj.sum_region(row1, col1, row2, col2);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = NumMatrix::new(vec![vec![3, 0, 1, 4, 2], vec![5, 6, 3, 2, 1], vec![1, 2, 0, 1, 5], vec![4, 1, 0, 1, 7], vec![1, 0, 3, 0, 5]]);
        check_eq!(obj.sum_region(2, 1, 4, 3), 8);
        check_eq!(obj.sum_region(1, 1, 2, 2), 11);
        check_eq!(obj.sum_region(1, 2, 2, 4), 12);
    }
}
