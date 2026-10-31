"""
Sort Colors (LeetCode #75)
Difficulty: Medium
Tag: two_pointers

Problem Statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Examples:
Example 1:
    Input: nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Example 2:
    Input: nums = [2, 0, 1]
    Output: [0, 1, 2]

Example 3:
    Input: nums = [0]
    Output: [0]

Constraints:
- n == len(nums)
- 1 <= n <= 3000
- nums[i] is either 0, 1, or 2.

Follow-up:
Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(f"Test Case 1 Output: {nums1}")
    assert nums1 == [0, 0, 1, 1, 2, 2], f"Expected [0, 0, 1, 1, 2, 2], got {nums1}"

    # Test Case 2
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    print(f"Test Case 2 Output: {nums2}")
    assert nums2 == [0, 1, 2], f"Expected [0, 1, 2], got {nums2}"

    # Test Case 3
    nums3 = [0]
    solution.sortColors(nums3)
    print(f"Test Case 3 Output: {nums3}")
    assert nums3 == [0], f"Expected [0], got {nums3}"

    print("All test cases passed!")
