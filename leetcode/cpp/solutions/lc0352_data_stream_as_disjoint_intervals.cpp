// 352. Data Stream as Disjoint Intervals · Hard · https://leetcode.com/problems/data-stream-as-disjoint-intervals/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class SummaryRanges {
public:
    SummaryRanges() {
        TODO();
    }
    
    void addNum(int value) {
        TODO();
    }
    
    vector<vector<int>> getIntervals() {
        TODO();
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
// ---------------------------------------------------------------- tests

TEST(example_1) {
    SummaryRanges *obj = new SummaryRanges();
    obj->addNum(1);
    CHECK_EQ(obj->getIntervals(), (vector<vector<int>>{{1, 1}}));
    obj->addNum(3);
    CHECK_EQ(obj->getIntervals(), (vector<vector<int>>{{1, 1}, {3, 3}}));
    obj->addNum(7);
    CHECK_EQ(obj->getIntervals(), (vector<vector<int>>{{1, 1}, {3, 3}, {7, 7}}));
    obj->addNum(2);
    CHECK_EQ(obj->getIntervals(), (vector<vector<int>>{{1, 3}, {7, 7}}));
    obj->addNum(6);
    CHECK_EQ(obj->getIntervals(), (vector<vector<int>>{{1, 3}, {6, 7}}));
}
