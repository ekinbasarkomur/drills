// 478. Generate Random Point in a Circle · Medium · https://leetcode.com/problems/generate-random-point-in-a-circle/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class Solution {
public:
    Solution(double radius, double x_center, double y_center) {
        TODO();
    }
    
    vector<double> randPoint() {
        TODO();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    double radius = 1.0;
    double x_center = 0.0;
    double y_center = 0.0;
    Solution *obj = new Solution(radius, x_center, y_center);
    CHECK(near(obj->randPoint(), vector<double>{-0.02493, -0.38077}));
    CHECK(near(obj->randPoint(), vector<double>{0.82314, 0.38945}));
    CHECK(near(obj->randPoint(), vector<double>{0.36572, 0.17248}));
}
