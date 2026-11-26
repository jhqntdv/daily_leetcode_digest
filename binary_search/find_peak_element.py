"""
LeetCode 162: Find Peak Element
https://leetcode.com/problems/find-peak-element/

Difficulty: Medium
Tag: binary_search

Problem Statement:
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Examples:
Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
    Input: nums = [1, 2, 1, 3, 5, 6, 4]
    Output: 5 (or 1)
    Explanation: Your function can return either index number 1 where the peak element is 2,
                 or index number 5 where the peak element is 6.

Example 3:
    Input: nums = [1]
    Output: 0
    Explanation: nums[0] is strictly greater than its neighbors outside the array, so index 0 is a peak.

Constraints:
    * 1 <= nums.length <= 1000
    * -2^31 <= nums[i] <= 2^31 - 1
    * nums[i] != nums[i + 1] for all valid i.
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test 1
    nums1 = [1, 2, 3, 1]
    print(f"Test 1: nums = {nums1} -> Peak Index: {solution.findPeakElement(nums1)} (Expected: 2)")

    # Test 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(f"Test 2: nums = {nums2} -> Peak Index: {solution.findPeakElement(nums2)} (Expected: 1 or 5)")

    # Test 3
    nums3 = [1]
    print(f"Test 3: nums = {nums3} -> Peak Index: {solution.findPeakElement(nums3)} (Expected: 0)")
