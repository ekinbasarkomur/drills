// What LeetCode provides around a C++ solution, so its code compiles here unchanged:
// every standard header, `using namespace std;`, ListNode and TreeNode.
// Plus what the generated tests use:
//
//   build({1, 2, 3}) / to_vector(head)             linked lists      (list_node.hpp)
//   build_tree({1, nullopt, 2}) / to_level_order   binary trees      (tree_node.hpp)
//   deep_sort(v)                                   answers "in any order"
//   sort_outer(v)                                  same, outer list only (permutations)
//   near(a, b)                                     doubles, 1e-5
//   TODO()                                         the stub body of an unsolved problem
#pragma once

#include <algorithm>
#include <array>
#include <atomic>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <condition_variable>
#include <cstdint>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <mutex>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <semaphore>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include "list_node.hpp"
#include "tree_node.hpp"

using namespace std;

#define TODO() throw std::logic_error("not solved yet")

template <class T> T deep_sort(T v) { return v; }
template <class T> vector<T> deep_sort(vector<T> v) {
    for (auto &x : v)
        x = deep_sort(x);
    sort(v.begin(), v.end());
    return v;
}

template <class T> vector<T> sort_outer(vector<T> v) {
    sort(v.begin(), v.end());
    return v;
}

inline bool near(double a, double b) { return std::fabs(a - b) < 1e-5; }
inline bool near(const vector<double> &a, const vector<double> &b) {
    if (a.size() != b.size())
        return false;
    for (size_t i = 0; i < a.size(); ++i)
        if (!near(a[i], b[i]))
            return false;
    return true;
}
