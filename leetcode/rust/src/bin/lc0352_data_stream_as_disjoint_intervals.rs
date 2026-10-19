// 352. Data Stream as Disjoint Intervals · Hard · https://leetcode.com/problems/data-stream-as-disjoint-intervals/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct SummaryRanges {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SummaryRanges {

    fn new() -> Self {
        todo!()
    }
    
    fn add_num(&self, value: i32) {
        todo!()
    }
    
    fn get_intervals(&self) -> Vec<Vec<i32>> {
        todo!()
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj = SummaryRanges::new();
 * obj.add_num(value);
 * let ret_2: Vec<Vec<i32>> = obj.get_intervals();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = SummaryRanges::new();
        obj.add_num(1);
        let want: Vec<Vec<i32>> = vec![vec![1, 1]];
        assert_eq!(obj.get_intervals(), want);
        obj.add_num(3);
        let want: Vec<Vec<i32>> = vec![vec![1, 1], vec![3, 3]];
        assert_eq!(obj.get_intervals(), want);
        obj.add_num(7);
        let want: Vec<Vec<i32>> = vec![vec![1, 1], vec![3, 3], vec![7, 7]];
        assert_eq!(obj.get_intervals(), want);
        obj.add_num(2);
        let want: Vec<Vec<i32>> = vec![vec![1, 3], vec![7, 7]];
        assert_eq!(obj.get_intervals(), want);
        obj.add_num(6);
        let want: Vec<Vec<i32>> = vec![vec![1, 3], vec![6, 7]];
        assert_eq!(obj.get_intervals(), want);
    }
}
