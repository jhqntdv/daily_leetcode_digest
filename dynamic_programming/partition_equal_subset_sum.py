"""
Partition Equal Subset Sum (LeetCode #416)
Difficulty: Medium
Tag: Dynamic Programming

Problem Statement:
Given an integer array `nums`, return True if you can partition the array into two 
subsets such that the sum of the elements in both subsets is equal, or False otherwise.

Example 1:
Input: nums = [1, 5, 11, 5]
Output: True
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1, 2, 3, 5]
Output: False
Explanation: The array cannot be partitioned into equal sum subsets.

Example 3:
Input: nums = [1, 2, 5]
Output: False

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Write your code here
        pass


if __name__ == '__main__':
    sol = Solution()

    # Example 1
    nums1 = [1, 5, 11, 5]
    res1 = sol.canPartition(nums1)
    print(f"Example 1: Input: nums = {nums1} | Output: {res1} | Expected: True")

    # Example 2
    nums2 = [1, 2, 3, 5]
    res2 = sol.canPartition(nums2)
    print(f"Example 2: Input: nums = {nums2} | Output: {res2} | Expected: False")

    # Example 3
    nums3 = [1, 2, 5]
    res3 = sol.canPartition(nums3)
    print(f"Example 3: Input: nums = {nums3} | Output: {res3} | Expected: False")
