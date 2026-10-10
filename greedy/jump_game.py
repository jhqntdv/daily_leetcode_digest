"""
Title: Jump Game
Difficulty: Medium

Problem Statement:
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `True` if you can reach the last index, or `False` otherwise.

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3, 2, 1, 0, 4]
Output: False
Explanation: You will always arrive at index 3. Its maximum jump length is 0, which makes it impossible to reach the last index.

Example 3:
Input: nums = [0]
Output: True
Explanation: You are already at the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TODO: Implement your solution here
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Test 1: {sol.canJump(nums1)} (Expected: True)")

    # Test Case 2
    nums2 = [3, 2, 1, 0, 4]
    print(f"Test 2: {sol.canJump(nums2)} (Expected: False)")

    # Test Case 3
    nums3 = [0]
    print(f"Test 3: {sol.canJump(nums3)} (Expected: True)")
