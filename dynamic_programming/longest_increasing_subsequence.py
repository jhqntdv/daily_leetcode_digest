"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Test 1 Output: {solution.lengthOfLIS(nums1)} (Expected: 4)")

    # Test Case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"Test 2 Output: {solution.lengthOfLIS(nums2)} (Expected: 4)")

    # Test Case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"Test 3 Output: {solution.lengthOfLIS(nums3)} (Expected: 1)")
