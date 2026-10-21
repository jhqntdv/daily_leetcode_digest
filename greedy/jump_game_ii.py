"""
Jump Game II (LeetCode #45)
Difficulty: Medium
Tag: Greedy / Dynamic Programming

You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
  - 0 <= j <= nums[i]
  - i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Example 3:
Input: nums = [1,2,1,1,1]
Output: 3

Constraints:
  - 1 <= nums.length <= 10^4
  - 0 <= nums[i] <= 1000
  - It's guaranteed that you can reach nums[n - 1].
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Write your solution here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Test 1: nums = {nums1} -> Result: {sol.jump(nums1)} (Expected: 2)")

    # Test Case 2
    nums2 = [2, 3, 0, 1, 4]
    print(f"Test 2: nums = {nums2} -> Result: {sol.jump(nums2)} (Expected: 2)")

    # Test Case 3
    nums3 = [1, 2, 1, 1, 1]
    print(f"Test 3: nums = {nums3} -> Result: {sol.jump(nums3)} (Expected: 3)")
