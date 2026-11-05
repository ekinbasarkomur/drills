// 732. My Calendar III · Hard · https://leetcode.com/problems/my-calendar-iii/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyCalendarThree {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendarThree {

    fn new() -> Self {
        todo!()
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> i32 {
        todo!()
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj = MyCalendarThree::new();
 * let ret_1: i32 = obj.book(startTime, endTime);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyCalendarThree::new();
        check_eq!(obj.book(10, 20), 1);
        check_eq!(obj.book(50, 60), 1);
        check_eq!(obj.book(10, 40), 2);
        check_eq!(obj.book(5, 15), 3);
        check_eq!(obj.book(5, 10), 3);
        check_eq!(obj.book(25, 55), 3);
    }
}
