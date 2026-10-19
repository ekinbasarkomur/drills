// 622. Design Circular Queue · Medium · https://leetcode.com/problems/design-circular-queue/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyCircularQueue {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCircularQueue {

    fn new(k: i32) -> Self {
        todo!()
    }
    
    fn en_queue(&self, value: i32) -> bool {
        todo!()
    }
    
    fn de_queue(&self) -> bool {
        todo!()
    }
    
    fn front(&self) -> i32 {
        todo!()
    }
    
    fn rear(&self) -> i32 {
        todo!()
    }
    
    fn is_empty(&self) -> bool {
        todo!()
    }
    
    fn is_full(&self) -> bool {
        todo!()
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * let obj = MyCircularQueue::new(k);
 * let ret_1: bool = obj.en_queue(value);
 * let ret_2: bool = obj.de_queue();
 * let ret_3: i32 = obj.front();
 * let ret_4: i32 = obj.rear();
 * let ret_5: bool = obj.is_empty();
 * let ret_6: bool = obj.is_full();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyCircularQueue::new(3);
        assert_eq!(obj.en_queue(1), true);
        assert_eq!(obj.en_queue(2), true);
        assert_eq!(obj.en_queue(3), true);
        assert_eq!(obj.en_queue(4), false);
        assert_eq!(obj.rear(), 3);
        assert_eq!(obj.is_full(), true);
        assert_eq!(obj.de_queue(), true);
        assert_eq!(obj.en_queue(4), true);
        assert_eq!(obj.rear(), 4);
    }
}
