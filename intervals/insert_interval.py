from typing import List

"""
57. Insert Interval
Difficulty: Medium

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]`
represent the start and the end of the ith interval and `intervals` is sorted in ascending order by start_i.
You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by start_i
and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^5
- intervals is sorted by start_i in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Three-Phase Linear Scan.

        Approach:
        Since `intervals` is already sorted by start time:
        1. Add all intervals that end strictly before `newInterval` starts (`intervals[i][1] < new_start`).
        2. Merge all overlapping intervals (`intervals[i][0] <= new_end`) into `newInterval` by updating:
           `new_start = min(new_start, intervals[i][0])`
           `new_end = max(new_end, intervals[i][1])`
           Then append the merged `[new_start, new_end]`.
        3. Append all remaining intervals that start strictly after `new_end`.

        Complexity:
        - Time: O(n), single pass through `intervals`.
        - Space: O(n) for the output list (O(1) auxiliary space).
        """
        result: List[List[int]] = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval[0], newInterval[1]

        # Phase 1: Intervals completely before newInterval
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1

        # Phase 2: Overlapping intervals -> merge into [new_start, new_end]
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        result.append([new_start, new_end])

        # Phase 3: Intervals completely after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    print(f"Test 1: {sol.insert(intervals1, newInterval1)} (Expected: [[1, 5], [6, 9]])")

    # Test Case 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    print(f"Test 2: {sol.insert(intervals2, newInterval2)} (Expected: [[1, 2], [3, 10], [12, 16]])")

    # Test Case 3
    intervals3 = []
    newInterval3 = [5, 7]
    print(f"Test 3: {sol.insert(intervals3, newInterval3)} (Expected: [[5, 7]])")
