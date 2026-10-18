# Algorithms — C++

One file per problem in `solutions/`, named after the problem in snake_case.
Each file holds the solution *and* its tests, the same way the Rust and Python
projects do.

    make                       # build and run every problem
    make two_sum               # build and run just that one
    make clean                 # wipe build/

Start a new problem by copying the template:

    cp template.cpp solutions/two_sum.cpp

`include/test.hpp` is a tiny harness (no dependencies, no package manager). It
provides `TEST(name) { ... }`, `CHECK(expr)` and `CHECK_EQ(a, b)`, and it
defines `main()` for you -- so your solution file must not define one.
