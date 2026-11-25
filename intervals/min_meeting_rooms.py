"""
Meeting Rooms II

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`,
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2

Example 2:
Input: intervals = [[7, 10], [2, 4]]
Output: 1

Example 3:
Input: intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20]]
Output: 4

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    sol = Solution()

    # Example 1
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print(f"Example 1 Output: {sol.minMeetingRooms(intervals1)} (Expected: 2)")

    # Example 2
    intervals2 = [[7, 10], [2, 4]]
    print(f"Example 2 Output: {sol.minMeetingRooms(intervals2)} (Expected: 1)")

    # Example 3
    intervals3 = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20]]
    print(f"Example 3 Output: {sol.minMeetingRooms(intervals3)} (Expected: 4)")
