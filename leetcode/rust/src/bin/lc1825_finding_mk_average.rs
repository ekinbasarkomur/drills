// 1825. Finding MK Average · Hard · https://leetcode.com/problems/finding-mk-average/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MKAverage {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MKAverage {

    fn new(m: i32, k: i32) -> Self {
        todo!()
    }
    
    fn add_element(&self, num: i32) {
        todo!()
    }
    
    fn calculate_mk_average(&self) -> i32 {
        todo!()
    }
}

/**
 * Your MKAverage object will be instantiated and called as such:
 * let obj = MKAverage::new(m, k);
 * obj.add_element(num);
 * let ret_2: i32 = obj.calculate_mk_average();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MKAverage::new(3, 1);
        obj.add_element(3);
        obj.add_element(1);
        check_eq!(obj.calculate_mk_average(), -1);
        obj.add_element(10);
        check_eq!(obj.calculate_mk_average(), 3);
        obj.add_element(5);
        obj.add_element(5);
        obj.add_element(5);
        check_eq!(obj.calculate_mk_average(), 5);
    }
}
