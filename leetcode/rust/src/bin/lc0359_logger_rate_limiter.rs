// 359. Logger Rate Limiter · Easy · https://leetcode.com/problems/logger-rate-limiter/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Logger {

}


impl Logger {

    fn new() -> Self {
        todo!()
    }
    
    fn should_print_message(&self, timestamp: i32, message: String) -> bool {
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
        let mut obj = Logger::new();
        obj.should_print_message(1, "foo".to_string());
        obj.should_print_message(2, "bar".to_string());
        obj.should_print_message(3, "foo".to_string());
        obj.should_print_message(8, "bar".to_string());
        obj.should_print_message(10, "foo".to_string());
        obj.should_print_message(11, "foo".to_string());
    }
}
