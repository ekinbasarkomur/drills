// 346. Moving Average from Data Stream · Easy · https://leetcode.com/problems/moving-average-from-data-stream/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MovingAverage {

}


impl MovingAverage {

    fn new(size: i32) -> Self {
        todo!()
    }
    
    fn next(&self, val: i32) -> f64 {
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
        // Premium problem: the expected output is not public, so this only runs it.
        let mut obj = MovingAverage::new(3);
        obj.next(1);
        obj.next(10);
        obj.next(3);
        obj.next(5);
    }
}
