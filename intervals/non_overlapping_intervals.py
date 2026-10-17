"""
Title: Non-overlapping Intervals
Difficulty: Medium
Tag: intervals

Problem Statement:
Given an array of intervals `intervals` where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point (e.g., [1, 2] and [2, 3]) are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # Write your solution here
    pass


if __name__ == '__main__':
    # Example 1
    test1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(f"Test 1 Output: {eraseOverlapIntervals(test1)} (Expected: 1)")

    # Example 2
    test2 = [[1, 2], [1, 2], [1, 2]]
    print(f"Test 2 Output: {eraseOverlapIntervals(test2)} (Expected: 2)")

    # Example 3
    test3 = [[1, 2], [2, 3]]
    print(f"Test 3 Output: {eraseOverlapIntervals(test3)} (Expected: 0)")
