// A small test harness so the C++ files read like the Rust and Python ones.
// It defines main(), so your solution file must NOT define one.
//
//   TEST(name) { ... }   declares a test case
//   CHECK(expr)          fails the case if expr is false, keeps going
//   CHECK_EQ(a, b)       same, for anything with operator==
//
// Every check prints what it ran and what came back, so a passing run still
// shows the answers. A failing one adds what was wanted and where it happened.
#pragma once

#include <cstdio>
#include <exception>
#include <functional>
#include <iterator>
#include <optional>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>
#include <vector>

namespace tinytest {

// ---------------------------------------------------------------- printing

// Caps, so one test that uses the constraint ceiling (10^5 elements) does not
// bury the rest of the run in a single line.
inline constexpr size_t max_items = 20;   // elements shown per container
inline constexpr size_t max_chars = 120;  // characters shown per string
inline constexpr size_t max_line = 1000;  // characters shown per value

template <class T> struct is_pair : std::false_type {};
template <class A, class B> struct is_pair<std::pair<A, B>> : std::true_type {};

template <class T> struct is_optional : std::false_type {};
template <class T> struct is_optional<std::optional<T>> : std::true_type {};

// Anything iterable prints as a sequence: vector, array, deque, list, set, map.
template <class T, class = void> struct is_range : std::false_type {};
template <class T>
struct is_range<T, std::void_t<decltype(std::begin(std::declval<const T &>())),
                               decltype(std::end(std::declval<const T &>()))>> : std::true_type {};

// A key_type means an associative container, which reads better in braces.
template <class T, class = void> struct has_key : std::false_type {};
template <class T> struct has_key<T, std::void_t<typename T::key_type>> : std::true_type {};

template <class T, class = void> struct has_mapped : std::false_type {};
template <class T> struct has_mapped<T, std::void_t<typename T::mapped_type>> : std::true_type {};

// std::array is both a range and tuple-like; the range branch wins, so this
// only catches std::tuple (pairs have their own branch).
template <class T, class = void> struct is_tuple_like : std::false_type {};
template <class T>
struct is_tuple_like<T, std::void_t<decltype(std::tuple_size<T>::value)>> : std::true_type {};

// The shared ListNode / TreeNode are matched by shape, not by name, so this
// header stays independent of list_node.hpp and tree_node.hpp.
template <class T, class = void> struct is_list_node : std::false_type {};
template <class T>
struct is_list_node<T, std::void_t<decltype(std::declval<const T &>().val),
                                   decltype(std::declval<const T &>().next)>> : std::true_type {};

template <class T, class = void> struct is_tree_node : std::false_type {};
template <class T>
struct is_tree_node<T, std::void_t<decltype(std::declval<const T &>().val),
                                   decltype(std::declval<const T &>().left),
                                   decltype(std::declval<const T &>().right)>> : std::true_type {};

template <class T> std::string to_text(const T &v);

inline std::string quote(std::string_view s) {
    if (s.size() <= max_chars)
        return "\"" + std::string(s) + "\"";
    return "\"" + std::string(s.substr(0, max_chars)) + "\"... (" + std::to_string(s.size()) +
           " chars)";
}

inline std::string clip(const std::string &s) {
    if (s.size() <= max_line)
        return s;
    return s.substr(0, max_line) + "... (" + std::to_string(s.size()) + " chars)";
}

// A map entry prints as `key: value`; everything else as the element itself.
template <class T> std::string element_text(const T &e, bool entry) {
    if constexpr (is_pair<std::decay_t<T>>::value) {
        if (entry)
            return to_text(e.first) + ": " + to_text(e.second);
    }
    return to_text(e);
}

template <class R>
std::string join(const R &r, const char *open, const char *close, bool entries) {
    std::string out = open;
    size_t shown = 0;
    auto it = std::begin(r);
    auto last = std::end(r);
    for (; it != last && shown < max_items; ++it, ++shown) {
        if (shown)
            out += ", ";
        out += element_text(*it, entries);
    }
    if (it != last) {
        size_t rest = 0;
        for (; it != last; ++it)
            ++rest;
        out += ", ... (" + std::to_string(rest) + " more)";
    }
    return out + close;
}

template <class N> std::string list_text(const N *head) {
    std::string out;
    size_t shown = 0;
    const N *p = head;
    for (; p && shown < max_items; p = p->next, ++shown) {
        if (shown)
            out += " -> ";
        out += to_text(p->val);
    }
    // No length count here: the list may be cyclic, which several problems use.
    if (p)
        out += " -> ...";
    return "[" + out + "]";
}

// Level order, the way LeetCode writes a tree, with trailing nulls trimmed.
template <class N> std::string tree_text(const N *root) {
    std::vector<const N *> level{root};
    std::vector<std::string> cells;
    size_t i = 0;
    for (; i < level.size() && cells.size() < max_items; ++i) {
        if (!level[i]) {
            cells.push_back("null");
            continue;
        }
        cells.push_back(to_text(level[i]->val));
        level.push_back(level[i]->left);
        level.push_back(level[i]->right);
    }
    bool more = i < level.size();
    while (!more && !cells.empty() && cells.back() == "null")
        cells.pop_back();

    std::string out;
    for (size_t k = 0; k < cells.size(); ++k) {
        if (k)
            out += ", ";
        out += cells[k];
    }
    if (more)
        out += ", ...";
    return "[" + out + "]";
}

template <class T> std::string to_text(const T &v) {
    using U = std::decay_t<T>;
    if constexpr (std::is_same_v<U, bool>) {
        return v ? "true" : "false";
    } else if constexpr (std::is_same_v<U, char>) {
        return std::string("'") + v + "'";
    } else if constexpr (std::is_same_v<U, signed char> || std::is_same_v<U, unsigned char>) {
        return std::string("'") + static_cast<char>(v) + "'";
    } else if constexpr (std::is_same_v<U, std::string> || std::is_same_v<U, std::string_view>) {
        return quote(v);
    } else if constexpr (std::is_same_v<U, const char *> || std::is_same_v<U, char *>) {
        return v ? quote(v) : "null";
    } else if constexpr (std::is_same_v<U, std::nullptr_t>) {
        return "null";
    } else if constexpr (is_optional<U>::value) {
        return v ? to_text(*v) : "null";
    } else if constexpr (is_range<U>::value) {
        if constexpr (has_key<U>::value)
            return join(v, "{", "}", has_mapped<U>::value);
        else
            return join(v, "[", "]", false);
    } else if constexpr (is_pair<U>::value) {
        return "(" + to_text(v.first) + ", " + to_text(v.second) + ")";
    } else if constexpr (is_tuple_like<U>::value) {
        std::string out = "(";
        std::apply(
            [&](const auto &...xs) {
                size_t i = 0;
                ((out += (i++ ? ", " : "") + to_text(xs)), ...);
            },
            v);
        return out + ")";
    } else if constexpr (std::is_floating_point_v<U>) {
        char buf[48];
        std::snprintf(buf, sizeof buf, "%.10g", static_cast<double>(v));
        return buf;
    } else if constexpr (std::is_arithmetic_v<U>) {
        return std::to_string(v);
    } else if constexpr (std::is_pointer_v<U>) {
        using E = std::remove_cv_t<std::remove_pointer_t<U>>;
        if constexpr (is_tree_node<E>::value)
            return v ? tree_text(v) : "[]";
        else if constexpr (is_list_node<E>::value)
            return v ? list_text(v) : "[]";
        else
            return v ? "<node>" : "null";
    } else if constexpr (is_list_node<U>::value || is_tree_node<U>::value) {
        return to_text(&v);
    } else {
        return "<value>";
    }
}

// ---------------------------------------------------------------- harness

struct Case {
    std::string name;
    std::function<void()> fn;
};

inline std::vector<Case> &registry() {
    static std::vector<Case> r;
    return r;
}

struct Register {
    Register(const char *n, std::function<void()> f) {
        registry().push_back({n, f});
    }
};

inline int failures = 0;

inline void show(const char *expr, const std::string &got) {
    std::printf("  %s  ->  %s\n", expr, clip(got).c_str());
}

inline void wrong(const char *file, int line, const char *expr, const std::string &got,
                  const std::string &want) {
    std::printf("  %s\n    got:    %s\n    wanted: %s\n    FAILED at %s:%d\n", expr,
                clip(got).c_str(), clip(want).c_str(), file, line);
    ++failures;
}

inline void untrue(const char *file, int line, const char *expr) {
    std::printf("  %s  ->  false, wanted true\n    FAILED at %s:%d\n", expr, file, line);
    ++failures;
}

template <class A, class B>
void check_eq(const char *file, int line, const char *expr, const A &got, const B &want) {
    if (got == want)
        show(expr, to_text(got));
    else
        wrong(file, line, expr, to_text(got), to_text(want));
}

} // namespace tinytest

#define TEST(name)                                                             \
    static void name();                                                        \
    static tinytest::Register tinytest_reg_##name(#name, name);                \
    static void name()

#define CHECK(expr)                                                            \
    do {                                                                       \
        if (expr)                                                              \
            tinytest::show(#expr, "true");                                     \
        else                                                                   \
            tinytest::untrue(__FILE__, __LINE__, #expr);                       \
    } while (0)

#define CHECK_EQ(a, b) tinytest::check_eq(__FILE__, __LINE__, #a, (a), (b))

int main() {
    int failed = 0;
    int total = static_cast<int>(tinytest::registry().size());
    for (auto &c : tinytest::registry()) {
        int before = tinytest::failures;
        std::printf("\n--- %s ", c.name.c_str());
        for (int i = static_cast<int>(c.name.size()); i < 68; ++i)
            std::putchar('-');
        std::putchar('\n');
        try {
            c.fn();
        } catch (const std::exception &e) {
            std::printf("  threw: %s\n", e.what());
            ++tinytest::failures;
        }
        bool ok = tinytest::failures == before;
        std::printf("  %s\n", ok ? "ok" : "FAILED");
        if (!ok)
            ++failed;
    }
    std::printf("\ntest result: %s. %d passed; %d failed\n",
                failed ? "FAILED" : "ok", total - failed, failed);
    return failed ? 1 : 0;
}
