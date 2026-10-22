# Drills

LeetCode practice, kept in one place: every problem is one file per language, named by
its LeetCode id, holding LeetCode's own starter code, the solution, and tests that say
whether the solution is right.

The point is repetition: a problem can be solved again later, in another language, or
after forgetting it, so nothing is deleted once it is written, and each file keeps a link
back to the problem.

```
drills/
├── plan.toml              the order to solve things in: the single source
├── PROGRESS.md            generated from plan.toml and the tests (make progress)
├── Makefile               runs anything from here
├── scripts/
│   ├── new.py             scaffolds a problem from LeetCode's data   (make new)
│   ├── progress.py        status, PROGRESS.md, what's next            (make status/progress/next)
│   ├── run.py             one problem's tests                         (make 146, make rust-146)
│   ├── copy.py            a solution to the clipboard                 (make copy)
│   ├── sync.py            writes accepted LeetCode submissions in   (the vault's leetcode_sync)
│   ├── leetcode.py        LeetCode's public problem data, cached in .cache/
│   └── drills.py          what the scripts share: paths, plan, marker lines
└── leetcode/
    ├── rust/              Cargo package; src/bin/lc0146_lru_cache.rs, src/lib.rs = helpers
    ├── cpp/               Makefile; solutions/lc0146_lru_cache.cpp, include/ = helpers
    ├── python/            lc0146_lru_cache.py, _lc.py = LeetCode's namespace
    ├── pandas_track/      lc0595_big_countries.py           (parallel track; not `pandas/`, which would shadow the library)
    ├── sql/               lc0584_find_customer_referee.sql  (parallel track, run on DuckDB)
    └── pyproject.toml     one uv project for python/, pandas_track/ and sql/
```

## The plan

[`plan.toml`](plan.toml) holds every problem, in the order to solve them. Phases
(`[[phase]]`) are solved in order, groups inside a phase in order, problems top to bottom.
Phase 0 holds the basics the later phases build on, picked by looking at those problems
(the NeetCode set this repo started with, plus one or two per missing pattern, each with a
`why` naming the later problems it prepares); the later phases come from what quant and
trading firms are known to ask, each problem with a `why`. Problems marked
`warmup = true` were not in the research; they are the direct prerequisite of the problem
after them.

Two `[[parallel]]` tracks run alongside, one problem a day: **Pandas** (LeetCode's
"Introduction to Pandas" / "30 Days of Pandas") and **SQL** ("SQL 50" plus a few
finance-flavoured extras).

Every plan problem is already scaffolded, in Rust, C++ and Python for the algorithm
phases and in pandas or SQL for the tracks. A problem outside the plan is one command
away: `make new 1768`.

## The Python environment

One [uv](https://docs.astral.sh/uv/) project at the repository root covers all
three Python tracks: `pyproject.toml`, `uv.lock` and `.venv` live here, not
inside `leetcode/`. `uv run` builds it on first use; there is nothing to
activate.

```
uv sync          install/refresh it
uv run pytest    every Python, pandas and SQL test
```

**Never move a `.venv` with `mv`.** The console scripts in `.venv/bin` hardcode
the interpreter's absolute path, so a moved venv leaves `uv run pytest` falling
back to an ephemeral environment — one with a different Python and none of this
project's dependencies, which shows up as `ModuleNotFoundError: duckdb` and
`TypeError: unsupported operand type(s) for |`. Delete it and `uv sync` again.

## Running things

```
make status          what is solved, per plan group (only changed files are re-tested)
make progress        the same, and rewrite PROGRESS.md
make next            the next problem to solve, per language and per parallel track
make 146             that problem's tests, in every language it has, full output
make rust-146        in Rust only  (also cpp-146, py-146, pandas-595, sql-584)
make new 146         scaffold any LeetCode id or slug; never overwrites a file
make copy 146 rust   put the solution on the clipboard, ready to paste into LeetCode
make rust            every Rust file, raw cargo output (also cpp, python, pandas, sql)
make clean           wipe build directories and the status cache
```

`make new ID=146 LANG=rust` and `make copy ID=146 LANG=rust` work too.

**Solved** means two things: the scaffold's stub is gone from the solution, and the file's
tests pass. Stub files are never run, and results are cached by file content in
`.cache/status.json`, so `make status` takes about a second when nothing changed.

Or from inside a project, with its own tool:

| | Everything | One problem |
| --- | --- | --- |
| **Rust** — `leetcode/rust/` | `cargo test` | `cargo test --bin lc0146_lru_cache` |
| **C++** — `leetcode/cpp/` | `make` | `make lc0146_lru_cache` |
| **Python, pandas, SQL** — `leetcode/` | `uv run pytest` | `uv run pytest python/lc0146_lru_cache.py` |

## The shape of a problem file

One problem, one file per language, named `lc<id, 4 digits>_<slug>`
(`lc0167_two_sum_ii_input_array_is_sorted.rs`; Cargo refuses binary names that start
with a digit, hence the `lc`). Every file has the same four parts:

1. **A header**: `146. LRU Cache · Medium · <url>`, the plan step it belongs to, and
   `Problem:` / `Approach:` / `Time O(?), space O(?)` lines for your own words.
2. **What LeetCode provides around the editor**: `use leetcode::*;` and
   `struct Solution;` in Rust, `#include "leetcode.hpp"` in C++, `from _lc import *` in
   Python. These give the file exactly the names LeetCode's judge has in scope
   (`ListNode`, `TreeNode`, `List`, `heapq`, every standard header, ...).
3. **The solution**, between two marker lines:

   ```
   // ---------------------------------------------------------------- solution
   impl Solution { ... }
   // ---------------------------------------------------------------- tests
   ```

   Everything between the markers is what goes into LeetCode's editor, and nothing else:
   `make copy` copies exactly that. `use std::...` lines belong inside, LeetCode needs
   them too.
4. **The tests**, below the second marker. A scaffold starts with the examples from the
   problem statement, generated from LeetCode's data; add the edge cases the statement
   does not show you (empty input, one element, the answer at the very end, duplicates,
   negative numbers, the value range's extremes).

A fresh scaffold holds LeetCode's starter code with a stub body: `todo!()` in Rust,
`TODO();` in C++, `raise NotImplementedError` in Python and pandas, and a
`-- TODO: solve, then delete this line` line in SQL. While the stub is there the problem
counts as unsolved; the generated tests fail until the solution is right.

How the tests are generated:

- inputs come from LeetCode's example test cases, outputs from the statement's
  `Output:` lines, types from the problem's signature metadata;
- a `void` function is checked through its (mutated) first argument;
- "in any order" in the statement means both sides are sorted before comparing (only the
  outer list for permutations); doubles compare to 1e-5; lists and trees are compared as
  their level-order values;
- design problems (`LRUCache`, `MedianFinder`, ...) construct the object and replay the
  example's calls, checking every non-null output; methods that are random by nature
  (`getRandom`, `pick`, `shuffle`) are called but not checked;
- premium problems have no public statement: the starter code is rebuilt from the
  signature, and the tests only run the example inputs;
- problems LeetCode judges with a custom harness (concurrency, `rand10`,
  serialize/deserialize, the two pandas problems that modify a table in place) get no
  generated tests; the file says so.

### Rust: `leetcode/rust/`

Every `.rs` file under `src/bin/` is its own binary with its own (empty) `main()`. No
`Cargo.toml` registration: drop the file in and it is runnable. `src/lib.rs` holds
LeetCode's `ListNode` and `TreeNode` verbatim, plus `build_list`, `list_to_vec`,
`build_tree`, `tree_to_vec`, `deep_sort`, `sort_outer`, `approx_eq`. `rand` is a
dependency because LeetCode's Rust has it.

LeetCode's Rust starter code for design problems takes `&self`; change it to `&mut self`
where the method mutates, as the comment in the snippet says. The tests work either way.

Linked List Cycle is the odd one: a cycle cannot be built out of `Option<Box<ListNode>>`,
so its Rust file uses an index-based arena instead (and LeetCode has no Rust version).

### C++: `leetcode/cpp/`

No CMake. The `Makefile` compiles each `solutions/*.cpp` separately with
`-std=c++20 -Wall -Wextra -O1`, using a precompiled `include/leetcode.hpp` (every
standard header, `using namespace std;`, `ListNode`, `TreeNode`), which keeps one
problem at about half a second.

`include/test.hpp` is a ~60 line harness providing `TEST(name)`, `CHECK(expr)` and
`CHECK_EQ(a, b)`, with Rust-shaped output; an exception thrown by the solution (the stub's
`TODO()` throws) counts as a failure. **It defines `main()`**, so a solution file must not.

### Python, pandas, SQL: `leetcode/`

One [uv](https://docs.astral.sh/uv/) project; `uv run` builds the virtualenv on first
use. pytest collects every `lc*.py` under `python/` and `pandas/`, and every `lc*.sql`
under `sql/` through `sql/conftest.py`.

- `python/_lc.py` is LeetCode's namespace (`typing`, `collections`, `heapq`, `bisect`,
  `ListNode`, `TreeNode`, ...) plus the test helpers `build`, `to_list`, `build_tree`,
  `to_level_order`, `deep_sorted`, `close`.
- `python/_pd.py` builds the input tables with LeetCode's dtypes (`frame`) and compares a
  result the way LeetCode's judge does (`check`: same columns, same rows, in any order
  unless the statement says "ordered by").
- An SQL file holds the query between the markers and, below them, the schema, each
  example's tables (`-- case:`) and the expected result (`-- expect:`). The query runs on
  [DuckDB](https://duckdb.org/), not MySQL: backticks, `#` comments and a handful of
  MySQL functions (`DATEDIFF`, `DATE_FORMAT`, `DATE_ADD`/`DATE_SUB`, `IF`, `CHAR_LENGTH`,
  `GROUP_CONCAT ... SEPARATOR`) are translated, but other MySQL-only syntax can fail
  here although LeetCode accepts it, and string comparison is case-sensitive here.

## LeetCode and Obsidian

The Obsidian vault (`~/Archive`, `Sources/Drills`) keeps one note per problem. Its
`leetcode_sync.py` pulls the latest accepted LeetCode submission per language and writes
it into the matching file here, between the markers, then runs that file's tests and
commits (`LeetCode sync: 146 rust, 23 cpp`), all through `scripts/sync.py`. A submission
is written only when it is newer than what the file holds (the last synced submission,
recorded in `.cache/synced.json`, or else the file's last commit; a stub always takes it),
a file with uncommitted changes is skipped, and nothing is ever pushed. Everything else in
this repo is written by hand.

## Formatting

4-space indentation everywhere, enforced by `.editorconfig`, plus `.clang-format` for
C++. Makefiles need a literal tab to start a recipe line.
