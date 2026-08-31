// <NUMBER>. <TITLE>            https://leetcode.com/problems/<slug>/
//
// Problem: one or two lines, in your own words.
// Approach: the trick in one line. Time O(?), space O(?).

// The solution is a plain function so the tests can call it.
fn solve(nums: &[i32], target: i32) -> Vec<i32> {
    let _ = (nums, target);
    todo!()
}

// Scratch area: run it by hand with `cargo run --bin _template`.
fn main() {
    println!("{:?}", solve(&[2, 7, 11, 15], 9));
}

// The real check. `cargo test --bin _template`
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        assert_eq!(solve(&[2, 7, 11, 15], 9), vec![0, 1]);
    }

    #[test]
    fn example_2() {
        assert_eq!(solve(&[3, 2, 4], 6), vec![1, 2]);
    }
}
