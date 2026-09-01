# NeetCode 150

The [NeetCode 150](https://neetcode.io/practice) problem set, solved in **Rust**,
**Python** and **C++**. One repository, three sibling projects, one shared shape.

The point of doing the same problem three times is not the problem — it is
watching the same idea come out differently in three type systems.

```
neetcode150/
├── README.md            you are here
├── rust-solutions/      cargo
├── python-solutions/    uv + pytest
└── cpp-solutions/       make + a hand-rolled test header
```

## Quick reference

| | Run everything | Run one problem | Start a new problem |
| --- | --- | --- | --- |
| **Rust** | `cargo test` | `cargo test --bin two_sum` | `cp template.rs src/bin/two_sum.rs` |
| **Python** | `uv run pytest` | `uv run pytest -k two_sum` | `cp template.py solutions/two_sum.py` |
| **C++** | `make` | `make two_sum` | `cp template.cpp solutions/two_sum.cpp` |

All three commands are run from inside that project's own directory.

## The shape every solution file follows

Whatever the language, a problem lives in **one file** named after the problem in
`snake_case`, and that file holds four things in this order:

1. **A header comment** — problem number, title, LeetCode URL, the problem in
   your own words, the approach in one line, and the time/space complexity.
2. **The solution function**, kept separate from any scratch/`main` code so the
   tests can call it.
3. **The tests** — the examples from the problem statement first, then the edge
   cases the statement does not show you.
4. **Optionally a scratch entry point** for printing things by hand.

Tests live *beside* the solution rather than in a separate `tests/` tree. That is
Rust's native convention (`#[cfg(test)] mod tests`), and the other two projects
were configured to match it so that all three feel the same.

### Why tests instead of a `main` that prints

NeetCode's own editor gives you a Run button and a fixed set of cases. Running
things here by hand and eyeballing `println!` output is strictly worse than that.
Writing the examples as assertions gets you the Run button *plus* every edge case
you thought of yourself, re-checked in a second, forever.

The edge cases matter more than the examples. A LeetCode statement shows you two
happy paths; the cases that actually break a solution are the empty input, the
single element, the answer sitting at the very end, duplicate values, negative
numbers, and the value range's extremes. Those go in the file too.

## Language-specific notes

### Rust — `rust-solutions/`

Every `.rs` file under `src/bin/` is its own standalone program with its own
`main()`. No `Cargo.toml` registration: drop the file in and it is runnable.

```
cargo test  --bin two_sum      run its tests
cargo run   --bin two_sum      run its main()
cargo check --bin two_sum      typecheck only, fastest feedback
```

Solutions keep LeetCode's `impl Solution` shape, with a `struct Solution;`
declared above it, so code can be pasted back into the LeetCode editor unchanged.
The one thing LeetCode hides from you is imports — `use std::collections::HashMap;`
and friends have to be written out here.

`src/main.rs` is not a solution, just a signpost.

### Python — `python-solutions/`

Managed with [uv](https://docs.astral.sh/uv/). `uv run` builds the virtualenv on
first use; there is nothing to activate.

```
uv run pytest                        every problem
uv run pytest -k two_sum             by name
uv run pytest solutions/two_sum.py   by path
uv run pytest -x -q                  stop at first failure, quiet
uv run python solutions/two_sum.py   run the __main__ scratch block
```

pytest normally only collects files named `test_*.py`. `pyproject.toml` overrides
that with `python_files = ["*.py"]` so it picks up the `test_*` functions living
inside each solution file — that is what keeps the layout identical to Rust's.

### C++ — `cpp-solutions/`

No CMake, no package manager. A `Makefile` globs `solutions/*.cpp` and compiles
each one separately with `-std=c++20 -Wall -Wextra -O2`.

```
make                 build and run every problem
make two_sum         build and run just that one
make clean           wipe build/
```

`include/test.hpp` is a ~40 line dependency-free harness providing `TEST(name)`,
`CHECK(expr)` and `CHECK_EQ(a, b)`, with output shaped to look like Rust's:

```
test example_1 ... ok
test empty_array ... ok

test result: ok. 6 passed; 0 failed
```

**It defines `main()` for you**, so a solution file must not define one. To print
something by hand, put the `printf` inside a `TEST`.

## Progress

✅ solved &nbsp;&nbsp; ▢ scaffolded — file, header and tests are in place, the
solution function is still a stub

| # | Problem | Rust | Python | C++ |
| --- | --- | :---: | :---: | :---: |
| 217 | Contains Duplicate | ✅ | ✅ | ✅ |
| 242 | Valid Anagram | ✅ | ▢ | ▢ |
| 1 | Two Sum | ✅ | ▢ | ▢ |
| 49 | Group Anagrams | ✅ | ▢ | ▢ |
| 347 | Top K Frequent Elements | ✅ | ▢ | ▢ |
| 271 | Encode and Decode Strings | ✅ | ▢ | ▢ |
| 238 | Product of Array Except Self | ✅ | ✅ | ▢ |
| 36 | Valid Sudoku | ✅ | ✅ | ▢ |
| 128 | Longest Consecutive Sequence | ✅ | ✅ | ▢ |
| 125 | Valid Palindrome | ▢ | ✅ | ▢ |
| 167 | Two Sum II - Input Array Is Sorted | ▢ | ▢ | ▢ |

A scaffolded file is ready to be solved: the problem statement, the approach
placeholder, and every test case are already written, including the edge cases
the LeetCode statement does not show you. Only the function body is missing.

## The Rust notebook

Kept outside this repo, in the Obsidian vault:

    ~/Archive/Sources/Courses/W3 Schools Rust Tutorial/Notes.md

A running reference, currently §1 through §106, covering the language from
`println!` being a macro through ownership, borrowing, collections, structs and
enums. Each entry is deliberately one line of rule plus one minimal example — a
lookup table, not a tutorial.
