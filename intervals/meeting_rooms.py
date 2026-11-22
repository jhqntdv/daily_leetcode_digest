"""
Title: Meeting Rooms
Difficulty: Easy
Tag: intervals

Problem Statement:
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], 
determine if a person could attend all meetings.

Note:
Meetings that end when another meeting starts (e.g., [1, 5] and [5, 10]) do not overlap.

Example 1:
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: False

Example 2:
Input: intervals = [[7, 10], [2, 4]]
Output: True

Example 3:
Input: intervals = [[1, 5], [5, 10]]
Output: True

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6
"""

from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Determines if a person can attend all meetings without overlap.
    """
    # Write your solution here
    pass


if __name__ == '__main__':
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([[1, 5], [5, 10]], True),
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = can_attend_meetings([list(interval) for interval in intervals])
        print(f"Test Case {i}: {'PASSED' if result == expected else 'FAILED'}")
        print(f"  Input: {intervals}")
        print(f"  Expected: {expected}, Got: {result}\n")
