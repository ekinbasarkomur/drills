// A ~40 line test harness so the C++ files read like the Rust and Python ones.
// It defines main(), so your solution file must NOT define one.
//
//   TEST(name) { ... }   declares a test case
//   CHECK(expr)          fails the case if expr is false, keeps going
//   CHECK_EQ(a, b)       same, for anything with operator==
#pragma once

#include <cstdio>
#include <functional>
#include <string>
#include <vector>

namespace tinytest {

struct Case {
    std::string name;
    std::function<void()> fn;
};

inline std::vector<Case> &registry() {
    static std::vector<Case> r;
    return r;
}

struct Register {
    Register(const char *n, std::function<void()> f) { registry().push_back({n, f}); }
};

inline int failures = 0;

inline void fail(const char *file, int line, const char *expr) {
    std::printf("    assertion failed: %s   (%s:%d)\n", expr, file, line);
    ++failures;
}

}  // namespace tinytest

#define TEST(name)                                                    \
    static void name();                                               \
    static tinytest::Register tinytest_reg_##name(#name, name);       \
    static void name()

#define CHECK(expr) \
    do { if (!(expr)) tinytest::fail(__FILE__, __LINE__, #expr); } while (0)

#define CHECK_EQ(a, b) \
    do { if (!((a) == (b))) tinytest::fail(__FILE__, __LINE__, #a " == " #b); } while (0)

int main() {
    int failed = 0;
    int total = static_cast<int>(tinytest::registry().size());
    for (auto &c : tinytest::registry()) {
        int before = tinytest::failures;
        c.fn();
        bool ok = tinytest::failures == before;
        std::printf("test %s ... %s\n", c.name.c_str(), ok ? "ok" : "FAILED");
        if (!ok) ++failed;
    }
    std::printf("\ntest result: %s. %d passed; %d failed\n",
                failed ? "FAILED" : "ok", total - failed, failed);
    return failed ? 1 : 0;
}
