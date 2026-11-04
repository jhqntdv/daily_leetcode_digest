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
    """
    Greedy Interval Scheduling (Sort by End Time).

    Approach:
    - Minimizing the number of removed intervals is equivalent to maximizing the number
      of non-overlapping intervals we keep.
    - Sort intervals by their **end time** (`key=lambda x: x[1]`).
    - Greedily keep the interval that finishes earliest to leave the maximum possible
      room for future intervals:
        - Track `prev_end` of the last kept interval.
        - For each `[start, end]`:
            - If `start < prev_end`, there is an overlap -> increment `removed` count
              (we discard the current interval because its `end >= prev_end`).
            - Otherwise (`start >= prev_end`), keep it and update `prev_end = end`.

    Complexity:
    - Time: O(n log n) due to sorting.
    - Space: O(1) auxiliary space (or O(n) for Timsort).
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    removed = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end

    return removed


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
