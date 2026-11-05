// 2034. Stock Price Fluctuation  · Medium · https://leetcode.com/problems/stock-price-fluctuation/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct StockPrice {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockPrice {

    fn new() -> Self {
        todo!()
    }
    
    fn update(&self, timestamp: i32, price: i32) {
        todo!()
    }
    
    fn current(&self) -> i32 {
        todo!()
    }
    
    fn maximum(&self) -> i32 {
        todo!()
    }
    
    fn minimum(&self) -> i32 {
        todo!()
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice::new();
 * obj.update(timestamp, price);
 * let ret_2: i32 = obj.current();
 * let ret_3: i32 = obj.maximum();
 * let ret_4: i32 = obj.minimum();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = StockPrice::new();
        obj.update(1, 10);
        obj.update(2, 5);
        check_eq!(obj.current(), 5);
        check_eq!(obj.maximum(), 10);
        obj.update(1, 3);
        check_eq!(obj.maximum(), 5);
        obj.update(4, 2);
        check_eq!(obj.minimum(), 2);
    }
}
