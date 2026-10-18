#!/usr/bin/env bash
# Print which exercises are solved in which language, by running their tests.
# Usage: scripts/status.sh [name ...]   (no arguments = all of them)
set -uo pipefail
cd "$(dirname "$0")/.."

names=("$@")
if [ ${#names[@]} -eq 0 ]; then
    for f in algorithms/cpp/solutions/*.cpp; do
        names+=("$(basename "$f" .cpp)")
    done
fi

tick() { [ "$1" = ok ] && printf '  ok ' || printf '  -- '; }

printf '%-42s %5s %7s %5s\n' EXERCISE rust python cpp
printf '%-42s %5s %7s %5s\n' "------------------------------------------" ----- ------- -----

rust_n=0; py_n=0; cpp_n=0; total=0
for n in "${names[@]}"; do
    total=$((total + 1))

    r=--
    if [ -f "algorithms/rust/src/bin/$n.rs" ] && \
       (cd algorithms/rust && cargo test --quiet --bin "$n" 2>&1 | grep -q '^test result: ok'); then
        r=ok; rust_n=$((rust_n + 1))
    fi

    p=--
    if [ -f "algorithms/python/solutions/$n.py" ] && \
       (cd algorithms/python && uv run pytest -q "solutions/$n.py" >/dev/null 2>&1); then
        p=ok; py_n=$((py_n + 1))
    fi

    c=--
    if [ -f "algorithms/cpp/solutions/$n.cpp" ] && \
       make -C algorithms/cpp --no-print-directory "$n" 2>&1 | grep -q '^test result: ok'; then
        c=ok; cpp_n=$((cpp_n + 1))
    fi

    printf '%-42s %5s %7s %5s\n' "$n" "$r" "$p" "$c"
done

printf '%-42s %5s %7s %5s\n' "------------------------------------------" ----- ------- -----
printf '%-42s %4s/%d %6s/%d %4s/%d\n' "solved" "$rust_n" "$total" "$py_n" "$total" "$cpp_n" "$total"
