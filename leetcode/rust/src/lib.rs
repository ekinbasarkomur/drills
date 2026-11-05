//! What LeetCode provides around a Rust solution, plus the helpers the tests use.
//!
//! Every problem file does `use leetcode::*;`, so ListNode, TreeNode, Rc and RefCell are in
//! scope exactly as on LeetCode, and the tests can build inputs from plain values:
//!
//!   build_list(&[1, 2, 3])                    -> Option<Box<ListNode>>
//!   list_to_vec(&head)                         -> Vec<i32>
//!   build_tree(&[Some(1), None, Some(2)])      -> level order, None = missing child
//!   tree_to_vec(&root)                         -> back to level order, trailing Nones trimmed
//!   deep_sort(v)                               -> for answers "in any order"
//!   sort_outer(v)                              -> same, but only the outer list (permutations)
//!   approx_eq(a, b) / approx_eq_vec(&a, &b)    -> doubles, 1e-5

pub use std::cell::RefCell;
pub use std::rc::Rc;

// LeetCode's definitions, verbatim.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode { val, left: None, right: None }
    }
}

pub fn build_list(values: &[i32]) -> Option<Box<ListNode>> {
    let mut head = None;
    for &v in values.iter().rev() {
        head = Some(Box::new(ListNode { val: v, next: head }));
    }
    head
}

pub fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {
    let mut out = Vec::new();
    let mut cur = head;
    while let Some(node) = cur {
        out.push(node.val);
        cur = &node.next;
    }
    out
}

pub fn build_tree(values: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    let root = Rc::new(RefCell::new(TreeNode::new(values.first().copied().flatten()?)));
    let mut queue = std::collections::VecDeque::from([root.clone()]);
    let mut i = 1;
    while i < values.len() {
        let Some(node) = queue.pop_front() else { break };
        for side in 0..2 {
            if let Some(Some(v)) = values.get(i) {
                let child = Rc::new(RefCell::new(TreeNode::new(*v)));
                queue.push_back(child.clone());
                if side == 0 {
                    node.borrow_mut().left = Some(child);
                } else {
                    node.borrow_mut().right = Some(child);
                }
            }
            i += 1;
        }
    }
    Some(root)
}

pub fn tree_to_vec(root: &Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<i32>> {
    let mut out = Vec::new();
    let mut queue = std::collections::VecDeque::from([root.clone()]);
    while let Some(node) = queue.pop_front() {
        match node {
            Some(n) => {
                let n = n.borrow();
                out.push(Some(n.val));
                queue.push_back(n.left.clone());
                queue.push_back(n.right.clone());
            }
            None => out.push(None),
        }
    }
    while out.last() == Some(&None) {
        out.pop();
    }
    out
}

/// Sorts a value and everything inside it, so two answers "in any order" compare equal.
pub trait DeepSort {
    fn deep_sort(self) -> Self;
}

macro_rules! leaf {
    ($($t:ty),*) => { $(impl DeepSort for $t { fn deep_sort(self) -> Self { self } })* };
}
leaf!(i32, i64, bool, char, String);

impl<T: DeepSort + Ord> DeepSort for Vec<T> {
    fn deep_sort(self) -> Self {
        let mut v: Vec<T> = self.into_iter().map(DeepSort::deep_sort).collect();
        v.sort();
        v
    }
}

pub fn deep_sort<T: DeepSort>(v: T) -> T {
    v.deep_sort()
}

pub fn approx_eq(a: f64, b: f64) -> bool {
    (a - b).abs() < 1e-5
}

/// Sorts only the outer list: answers "in any order" whose items are themselves ordered
/// (permutations).
pub fn sort_outer<T: Ord>(mut v: Vec<T>) -> Vec<T> {
    v.sort();
    v
}

pub fn approx_eq_vec(a: &[f64], b: &[f64]) -> bool {
    a.len() == b.len() && a.iter().zip(b).all(|(x, y)| approx_eq(*x, *y))
}

/// The test name libtest gave this thread, to name the case in a failure.
pub fn case_name() -> String {
    std::thread::current()
        .name()
        .unwrap_or("test")
        .rsplit("::")
        .next()
        .unwrap_or("test")
        .to_string()
}

/// Breaks the line once per test, before that test's first printed result.
/// Under `--nocapture` libtest leaves `test tests::example_1 ... ` open on its line, so
/// without this the first result lands on it and pushes `ok` onto a line of its own;
/// with it the name, the results and the verdict read as one block.
pub fn start_case(case: &str) {
    static LAST: std::sync::Mutex<Option<String>> = std::sync::Mutex::new(None);
    let mut last = LAST.lock().unwrap_or_else(|e| e.into_inner());
    if last.as_deref() != Some(case) {
        println!();
        *last = Some(case.to_string());
    }
}

/// `check_eq!(got, want)` is `assert_eq!` that also prints on the way through,
/// so a passing run still shows every answer. Needs `cargo test -- --nocapture`,
/// which `make rust-<id>` already passes.
#[macro_export]
macro_rules! check_eq {
    ($got:expr, $want:expr $(,)?) => {{
        let got = $got;
        let want = $want;
        if got == want {
            $crate::start_case(&$crate::case_name());
            println!("  {}  ->  {:?}", stringify!($got), got);
        } else {
            panic!(
                "{}: wrong answer\n  {}\n    got:    {:?}\n    wanted: {:?}",
                $crate::case_name(),
                stringify!($got),
                got,
                want
            );
        }
    }};
}

/// `check!(expr)` is `assert!` that prints what it ran.
#[macro_export]
macro_rules! check {
    ($cond:expr $(,)?) => {{
        if $cond {
            $crate::start_case(&$crate::case_name());
            println!("  {}  ->  true", stringify!($cond));
        } else {
            panic!(
                "{}: wrong answer\n  {}\n    got:    false\n    wanted: true",
                $crate::case_name(),
                stringify!($cond)
            );
        }
    }};
}
