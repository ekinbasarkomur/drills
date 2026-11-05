// 641. Design Circular Deque · Medium · https://leetcode.com/problems/design-circular-deque/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyCircularDeque {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCircularDeque {

    fn new(k: i32) -> Self {
        todo!()
    }
    
    fn insert_front(&self, value: i32) -> bool {
        todo!()
    }
    
    fn insert_last(&self, value: i32) -> bool {
        todo!()
    }
    
    fn delete_front(&self) -> bool {
        todo!()
    }
    
    fn delete_last(&self) -> bool {
        todo!()
    }
    
    fn get_front(&self) -> i32 {
        todo!()
    }
    
    fn get_rear(&self) -> i32 {
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
 * Your MyCircularDeque object will be instantiated and called as such:
 * let obj = MyCircularDeque::new(k);
 * let ret_1: bool = obj.insert_front(value);
 * let ret_2: bool = obj.insert_last(value);
 * let ret_3: bool = obj.delete_front();
 * let ret_4: bool = obj.delete_last();
 * let ret_5: i32 = obj.get_front();
 * let ret_6: i32 = obj.get_rear();
 * let ret_7: bool = obj.is_empty();
 * let ret_8: bool = obj.is_full();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyCircularDeque::new(3);
        check_eq!(obj.insert_last(1), true);
        check_eq!(obj.insert_last(2), true);
        check_eq!(obj.insert_front(3), true);
        check_eq!(obj.insert_front(4), false);
        check_eq!(obj.get_rear(), 2);
        check_eq!(obj.is_full(), true);
        check_eq!(obj.delete_last(), true);
        check_eq!(obj.insert_front(4), true);
        check_eq!(obj.get_front(), 4);
    }
}
