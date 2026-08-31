# NeetCode 150

One file per problem in `src/bin/`, named after the problem in snake_case.

    cargo run  --bin two_sum     # run main(), print scratch output
    cargo test --bin two_sum     # run that problem's tests
    cargo test                   # run every test in the repo
    cargo check --bin two_sum    # typecheck only, fastest feedback

Start a new problem by copying the template:

    cp src/bin/_template.rs src/bin/two_sum.rs

Each file has three parts: a header comment with the problem link and the
approach, a `solve()` function holding the actual answer, and a `#[cfg(test)]`
module with the examples from the problem statement as test cases.
