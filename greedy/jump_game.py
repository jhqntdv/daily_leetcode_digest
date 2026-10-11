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
        """
        Greedy approach:
        Maintain the farthest index reachable (`max_reach`).
        If at any point the current index `i` exceeds `max_reach`, we cannot proceed.
        If `max_reach` reaches or exceeds the last index, return True immediately.

        Time Complexity: O(n) - single pass through the array.
        Space Complexity: O(1) - only constant extra space.
        """
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    res1 = sol.canJump(nums1)
    print(f"Test 1: {res1} (Expected: True) -> {'PASS' if res1 is True else 'FAIL'}")

    # Test Case 2
    nums2 = [3, 2, 1, 0, 4]
    res2 = sol.canJump(nums2)
    print(f"Test 2: {res2} (Expected: False) -> {'PASS' if res2 is False else 'FAIL'}")

    # Test Case 3
    nums3 = [0]
    res3 = sol.canJump(nums3)
    print(f"Test 3: {res3} (Expected: True) -> {'PASS' if res3 is True else 'FAIL'}")

    # Test Case 4 (Edge case: cannot jump from start when length > 1)
    nums4 = [0, 2, 3]
    res4 = sol.canJump(nums4)
    print(f"Test 4: {res4} (Expected: False) -> {'PASS' if res4 is False else 'FAIL'}")
