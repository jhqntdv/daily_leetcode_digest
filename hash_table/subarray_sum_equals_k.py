"""
560. Subarray Sum Equals K
Difficulty: Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Example 3:
Input: nums = [1,-1,0], k = 0
Output: 3

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Write your solution here
        pass

if __name__ == '__main__':
    sol = Solution()

    # Example 1
    nums1, k1 = [1, 1, 1], 2
    print(f"Example 1: nums = {nums1}, k = {k1} -> Output: {sol.subarraySum(nums1, k1)} (Expected: 2)")

    # Example 2
    nums2, k2 = [1, 2, 3], 3
    print(f"Example 2: nums = {nums2}, k = {k2} -> Output: {sol.subarraySum(nums2, k2)} (Expected: 2)")

    # Example 3
    nums3, k3 = [1, -1, 0], 0
    print(f"Example 3: nums = {nums3}, k = {k3} -> Output: {sol.subarraySum(nums3, k3)} (Expected: 3)")
