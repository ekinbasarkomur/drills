// 33. Search in Rotated Sorted Array
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//
// Problem: nums was sorted ascending, then rotated some number of times.
//          Return the index of target, or -1. O(log n) is the point.
// Note: At any midpoint one of the two halves is still properly sorted.
//       Work out which, and you know whether target can be in it.
// Approach: binary search. At every midpoint one half is properly sorted;
//           if target falls inside that half's range search it, otherwise
//           search the other half.
// Time O(log n), space O(1)

#include <iostream>
#include <vector>

#include "test.hpp"

using namespace std;

class Solution {
public:
    int search(vector<int> &nums, int target) {
        int left = 0;
        int right = (int)nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
};

// ---------------------------------------------------------------- tests
// search takes a non-const reference, so it cannot be handed a temporary.

static int search(vector<int> nums, int target) {
    return Solution().search(nums, target);
}

TEST(example_1) { CHECK((search({3, 4, 5, 6, 1, 2}, 1) == 4)); }

TEST(example_2) { CHECK((search({3, 5, 6, 0, 1, 2}, 4) == -1)); }

TEST(single_element_found) { CHECK((search({1}, 1) == 0)); }

TEST(single_element_missing) { CHECK((search({1}, 2) == -1)); }

TEST(not_rotated_at_all) {
    // a full rotation looks like no rotation
    CHECK((search({1, 2, 3, 4, 5, 6}, 4) == 3));
}

TEST(target_is_the_pivot) { CHECK((search({4, 5, 6, 7, 0, 1, 2}, 0) == 4)); }

TEST(target_missing_inside_the_range) {
    CHECK((search({4, 5, 6, 7, 0, 1, 2}, 3) == -1));
}

TEST(rotated_by_one) { CHECK((search({2, 1}, 1) == 1)); }

TEST(target_is_the_first_element) { CHECK((search({5, 1, 2, 3, 4}, 5) == 0)); }

TEST(negative_values) { CHECK((search({0, 1, 2, -3, -2, -1}, -3) == 3)); }

TEST(largest_allowed_input) {
    // 1000 elements rotated so the smallest sits in the middle.
    // The answer is at index 0.
    vector<int> nums;
    for (int i = 500; i < 1000; ++i)
        nums.push_back(i);
    for (int i = 0; i < 500; ++i)
        nums.push_back(i);
    CHECK((search(nums, 500) == 0));
}
