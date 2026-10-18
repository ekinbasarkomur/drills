# Drills

Practice, kept in one place. Every exercise lives here with its source, its
solution, and tests that say whether the solution is right.

The point is repetition: a problem can be solved again later, in another
language, or after forgetting it — so nothing is deleted once it is written,
and each one keeps a link back to where it came from.

```
drills/
├── README.md            the index below
├── Makefile             runs anything from here
├── scripts/progress.py  writes the PROGRESS.md tables
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

| Track | Source | Languages | Solved | Progress |
| --- | --- | --- | --- | --- |
| [`algorithms/`](algorithms/) | [NeetCode 150](https://neetcode.io/practice) / [LeetCode](https://leetcode.com/) | Rust, Python, C++ | rust 11/34, python 5/34, cpp 18/34 | [PROGRESS.md](algorithms/PROGRESS.md) |
| [`pandas/`](pandas/) | not started | Python | — | [PROGRESS.md](pandas/PROGRESS.md) |
| [`machine-learning/`](machine-learning/) | not started | Python | — | [PROGRESS.md](machine-learning/PROGRESS.md) |
| [`rust-lang/`](rust-lang/) | not started | Rust | — | [PROGRESS.md](rust-lang/PROGRESS.md) |

## Running things

From the repository root, through the top-level `Makefile`:

```
make status          a grid of what is solved in which language (~15s)
make progress        the same, and rewrite the PROGRESS.md tables
make two_sum         that one exercise, in all three languages
make cpp-two_sum     that one exercise, in C++ only  (also rust- and py-)
make rust            every Rust exercise, raw cargo output
make python          every Python exercise, raw pytest output
make cpp             every C++ exercise
make list            the exercise names you can pass
make clean           wipe every build directory
```

`make status` is what the index below is generated from — it runs each
exercise's tests rather than reading the files, so it cannot drift.

Or from inside a project, with its own tool:

| | Everything | One exercise |
| --- | --- | --- |
| **Rust** — `algorithms/rust/` | `cargo test` | `cargo test --bin two_sum` |
| **Python** — `algorithms/python/` | `uv run pytest` | `uv run pytest -k two_sum` |
| **C++** — `algorithms/cpp/` | `make` | `make two_sum` |

The **File** column in the index below is the name to pass.

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

Each track keeps its own table, generated from its tests where it can be:

| Track | Progress |
| --- | --- |
| [`algorithms/PROGRESS.md`](algorithms/PROGRESS.md) | every problem, grouped by NeetCode section, linked to LeetCode, with a tick per language |
| [`pandas/PROGRESS.md`](pandas/PROGRESS.md) | not started |
| [`machine-learning/PROGRESS.md`](machine-learning/PROGRESS.md) | not started |
| [`rust-lang/PROGRESS.md`](rust-lang/PROGRESS.md) | not started |

`make progress` reruns every test and rewrites `algorithms/PROGRESS.md` plus
the totals in the table above, so neither can drift. The other three are
written by hand until their track has a runner.

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
