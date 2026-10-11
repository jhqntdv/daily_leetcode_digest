"""
Title: Subsets
Difficulty: Medium
Tag: Backtracking / Array

Problem Statement:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
Input: nums = [0]
Output: [[], [0]]

Example 3:
Input: nums = [1, 2]
Output: [[], [1], [2], [1, 2]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Test 1 Input: {nums1}")
    print(f"Test 1 Output: {sol.subsets(nums1)}")

    # Test Case 2
    nums2 = [0]
    print(f"Test 2 Input: {nums2}")
    print(f"Test 2 Output: {sol.subsets(nums2)}")

    # Test Case 3
    nums3 = [1, 2]
    print(f"Test 3 Input: {nums3}")
    print(f"Test 3 Output: {sol.subsets(nums3)}")
