# Drills

Practice, kept in one place. Every exercise lives here with its source, its
solution, and tests that say whether the solution is right.

The point is repetition: a problem can be solved again later, in another
language, or after forgetting it — so nothing is deleted once it is written,
and each one keeps a link back to where it came from.

```
drills/
├── README.md            the index below
├── algorithms/          LeetCode / NeetCode 150, in three languages
│   ├── rust/
│   ├── python/
│   └── cpp/
├── pandas/              (empty)
├── machine-learning/    (empty)
└── rust-lang/           (empty)
```

Each track brings its own toolchain and its own README. A new track is a new
top-level directory — it does not have to look like the others.

## Tracks

| Track | Source | Languages | Run |
| --- | --- | --- | --- |
| [`algorithms/`](algorithms/) | [NeetCode 150](https://neetcode.io/practice) / [LeetCode](https://leetcode.com/) | Rust, Python, C++ | see below |
| [`pandas/`](pandas/) | not started | Python | — |
| [`machine-learning/`](machine-learning/) | not started | Python | — |
| [`rust-lang/`](rust-lang/) | not started | Rust | — |

## Running things

| | Everything | One exercise |
| --- | --- | --- |
| **Rust** — `algorithms/rust/` | `cargo test` | `cargo test --bin two_sum` |
| **Python** — `algorithms/python/` | `uv run pytest` | `uv run pytest -k two_sum` |
| **C++** — `algorithms/cpp/` | `make` | `make two_sum` |

Each command is run from inside that project's own directory. The **File**
column in the index below is the name to pass.

## The shape every exercise follows

Whatever the track or language, one exercise is **one file** named in
`snake_case`, holding four things in this order:

1. **A header comment** — where the problem came from (number, title, URL),
   the problem in your own words, the approach in one line, and the
   time/space complexity.
2. **The solution**, kept separate from any scratch or `main` code so the
   tests can call it.
3. **The tests** — the examples from the problem statement first, then the
   edge cases the statement does not show you.
4. **Optionally a scratch entry point** for printing things by hand.

Tests live *beside* the solution rather than in a separate `tests/` tree. That
is Rust's native convention (`#[cfg(test)] mod tests`), and the other projects
were configured to match it so every track feels the same.

### Why tests instead of a `main` that prints

A practice site gives you a Run button and a fixed set of cases. Running
things by hand and eyeballing the output is strictly worse than that. Writing
the examples as assertions gets you the Run button *plus* every edge case you
thought of yourself, re-checked in a second, forever.

The edge cases matter more than the examples. A problem statement shows two
happy paths; what actually breaks a solution is the empty input, the single
element, the answer sitting at the very end, duplicate values, negative
numbers, and the value range's extremes. Those go in the file too.

## Index


### Arrays & Hashing

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [217](https://leetcode.com/problems/contains-duplicate/) | Contains Duplicate | ✅ | ✅ | ✅ | `contains_duplicate` |
| [242](https://leetcode.com/problems/valid-anagram/) | Valid Anagram | ✅ | ▢ | ✅ | `valid_anagram` |
| [1](https://leetcode.com/problems/two-sum/) | Two Sum | ✅ | ▢ | ✅ | `two_sum` |
| [49](https://leetcode.com/problems/group-anagrams/) | Group Anagrams | ✅ | ▢ | ✅ | `group_anagrams` |
| [347](https://leetcode.com/problems/top-k-frequent-elements/) | Top K Frequent Elements | ✅ | ▢ | ▢ | `top_k_frequent` |
| [271](https://leetcode.com/problems/encode-and-decode-strings/) | Encode and Decode Strings | ✅ | ▢ | ✅ | `encode_decode_strings` |
| [238](https://leetcode.com/problems/product-of-array-except-self/) | Product of Array Except Self | ✅ | ✅ | ✅ | `products_of_array_except_self` |
| [36](https://leetcode.com/problems/valid-sudoku/) | Valid Sudoku | ✅ | ✅ | ✅ | `valid_sudoku` |
| [128](https://leetcode.com/problems/longest-consecutive-sequence/) | Longest Consecutive Sequence | ✅ | ✅ | ✅ | `longest_consecutive_sequence` |

### Two Pointers

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [125](https://leetcode.com/problems/valid-palindrome/) | Valid Palindrome | ✅ | ✅ | ✅ | `valid_palindrome` |
| [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Sum II - Input Array Is Sorted | ✅ | ▢ | ✅ | `two_sum_ii` |
| [15](https://leetcode.com/problems/3sum/) | 3Sum | ▢ | ▢ | ✅ | `three_sum` |
| [11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water | ▢ | ▢ | ▢ | `container_with_most_water` |
| [42](https://leetcode.com/problems/trapping-rain-water/) | Trapping Rain Water | ▢ | ▢ | ▢ | `trapping_rain_water` |

### Sliding Window

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Best Time to Buy and Sell Stock | ▢ | ▢ | ✅ | `best_time_to_buy_and_sell_stock` |
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | ▢ | ▢ | ✅ | `longest_substring_without_repeating` |
| [424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Longest Repeating Character Replacement | ▢ | ▢ | ▢ | `longest_repeating_character_replacement` |

### Stack

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | ▢ | ▢ | ✅ | `valid_parentheses` |
| [155](https://leetcode.com/problems/min-stack/) | Min Stack | ▢ | ▢ | ✅ | `min_stack` |
| [739](https://leetcode.com/problems/daily-temperatures/) | Daily Temperatures | ▢ | ▢ | ▢ | `daily_temperatures` |

### Binary Search

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [704](https://leetcode.com/problems/binary-search/) | Binary Search | ▢ | ▢ | ▢ | `binary_search` |
| [875](https://leetcode.com/problems/koko-eating-bananas/) | Koko Eating Bananas | ▢ | ▢ | ▢ | `koko_eating_bananas` |
| [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Search in Rotated Sorted Array | ▢ | ▢ | ▢ | `search_in_rotated_sorted_array` |

### Linked List

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [206](https://leetcode.com/problems/reverse-linked-list/) | Reverse Linked List | ▢ | ▢ | ✅ | `reverse_linked_list` |
| [21](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge Two Sorted Lists | ▢ | ▢ | ✅ | `merge_two_sorted_lists` |
| [141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle | ▢ | ▢ | ▢ | `linked_list_cycle` |
| [146](https://leetcode.com/problems/lru-cache/) | LRU Cache | ▢ | ▢ | ▢ | `lru_cache` |

### Trees

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [226](https://leetcode.com/problems/invert-binary-tree/) | Invert Binary Tree | ▢ | ▢ | ▢ | `invert_binary_tree` |
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Maximum Depth of Binary Tree | ▢ | ▢ | ▢ | `maximum_depth_of_binary_tree` |

### Heap / Priority Queue

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Kth Largest Element in a Stream | ▢ | ▢ | ✅ | `kth_largest_element_in_a_stream` |
| [1046](https://leetcode.com/problems/last-stone-weight/) | Last Stone Weight | ▢ | ▢ | ▢ | `last_stone_weight` |

### Graphs

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | ▢ | ▢ | ▢ | `number_of_islands` |

### Greedy

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [53](https://leetcode.com/problems/maximum-subarray/) | Maximum Subarray | ▢ | ▢ | ▢ | `maximum_subarray` |

### Intervals

| # | Problem | Rust | Python | C++ | File |
| --- | --- | :---: | :---: | :---: | --- |
| [56](https://leetcode.com/problems/merge-intervals/) | Merge Intervals | ▢ | ▢ | ▢ | `merge_intervals` |

✅ solved &nbsp;&nbsp; ▢ scaffolded — the file, its header and all its tests are
in place, only the function body is missing.

Counts: **Rust 11/34**, **Python 5/34**, **C++ 18/34**.

A scaffolded file is ready to be solved: nothing is missing but the body. To
start one, open it and run that language's command above.

## Starting a new exercise

Copy the template in the language you want:

```
cp algorithms/rust/template.rs   algorithms/rust/src/bin/<name>.rs
cp algorithms/python/template.py algorithms/python/solutions/<name>.py
cp algorithms/cpp/template.cpp   algorithms/cpp/solutions/<name>.cpp
```

Then add a row to the index above with the source link.

## Language notes

### Rust — `algorithms/rust/`

Every `.rs` file under `src/bin/` is its own standalone program with its own
`main()`. No `Cargo.toml` registration: drop the file in and it is runnable.

```
cargo test  --bin two_sum      run its tests
cargo run   --bin two_sum      run its main()
cargo check --bin two_sum      typecheck only, fastest feedback
```

Solutions keep LeetCode's `impl Solution` shape, with a `struct Solution;`
declared above it, so code can be pasted back into the site unchanged. The one
thing those editors hide is imports — `use std::collections::HashMap;` and
friends have to be written out here.

`src/main.rs` is not a solution, just a signpost.

Linked-list and tree problems carry LeetCode's own type definition in the file
rather than sharing one, because the list is `Option<Box<ListNode>>` and the
tree `Option<Rc<RefCell<TreeNode>>>` — things to paste, not to share. Linked
List Cycle is the exception: a cycle cannot be built out of `Option<Box<..>>`
at all, so it uses an index-based arena instead.

### Python — `algorithms/python/`

Managed with [uv](https://docs.astral.sh/uv/). `uv run` builds the virtualenv
on first use; there is nothing to activate.

```
uv run pytest                        every exercise
uv run pytest -k two_sum             by name
uv run pytest solutions/two_sum.py   by path
uv run pytest -x -q                  stop at first failure, quiet
uv run python solutions/two_sum.py   run the __main__ scratch block
```

pytest normally only collects files named `test_*.py`. `pyproject.toml`
overrides that with `python_files = ["*.py"]` so it picks up the `test_*`
functions living inside each solution file.

`solutions/list_node.py` and `solutions/tree_node.py` are shared helpers, not
exercises; `pyproject.toml` excludes them from collection.

### C++ — `algorithms/cpp/`

No CMake, no package manager. A `Makefile` globs `solutions/*.cpp` and
compiles each one separately with `-std=c++20 -Wall -Wextra -O2`.

```
make                 build and run every exercise
make two_sum         build and run just that one
make clean           wipe build/
```

`include/test.hpp` is a ~40 line dependency-free harness providing
`TEST(name)`, `CHECK(expr)` and `CHECK_EQ(a, b)`, with output shaped to look
like Rust's:

```
test example_1 ... ok
test empty_array ... ok

test result: ok. 6 passed; 0 failed
```

**It defines `main()`**, so a solution file must not. To print something by
hand, put the `printf` inside a `TEST`.

`include/list_node.hpp` and `include/tree_node.hpp` hold the shared `ListNode`
and `TreeNode` types plus builders, so linked-list and tree problems keep
LeetCode's shape while the tests stay readable. They deliberately do **not**
carry `using namespace std;` — a header pulls the whole namespace into every
file that includes it.

## Formatting

4-space indentation everywhere, enforced by `.editorconfig`, plus
`.clang-format` for C++. The one exception is `algorithms/cpp/Makefile`: make
requires a literal tab to start a recipe line.

## The Rust notebook

Kept outside this repo, in the Obsidian vault:

```
~/Archive/Sources/Courses/W3 Schools Rust Tutorial/Notes.md
```

A running reference covering the language from `println!` being a macro
through ownership, borrowing, collections, structs and enums. Each entry is
deliberately one line of rule plus one minimal example — a lookup table, not a
tutorial.
