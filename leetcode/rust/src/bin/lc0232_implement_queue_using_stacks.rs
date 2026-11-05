// 232. Implement Queue using Stacks · Easy · https://leetcode.com/problems/implement-queue-using-stacks/
// Plan: Aşama 0 · Stack
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyQueue {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        todo!()
    }
    
    fn push(&self, x: i32) {
        todo!()
    }
    
    fn pop(&self) -> i32 {
        todo!()
    }
    
    fn peek(&self) -> i32 {
        todo!()
    }
    
    fn empty(&self) -> bool {
        todo!()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyQueue::new();
        obj.push(1);
        obj.push(2);
        check_eq!(obj.peek(), 1);
        check_eq!(obj.pop(), 1);
        check_eq!(obj.empty(), false);
    }
}
