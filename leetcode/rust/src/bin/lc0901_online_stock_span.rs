// 901. Online Stock Span · Medium · https://leetcode.com/problems/online-stock-span/
// Plan: Aşama 1 · Monotonic Stack ve Queue
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct StockSpanner {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {

    fn new() -> Self {
        todo!()
    }
    
    fn next(&self, price: i32) -> i32 {
        todo!()
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = StockSpanner::new();
        check_eq!(obj.next(100), 1);
        check_eq!(obj.next(80), 1);
        check_eq!(obj.next(60), 1);
        check_eq!(obj.next(70), 2);
        check_eq!(obj.next(60), 1);
        check_eq!(obj.next(75), 4);
        check_eq!(obj.next(85), 6);
    }
}
