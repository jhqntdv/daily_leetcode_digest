"""
Maximum Product Subarray

Difficulty: Medium

Problem Statement:
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Example 3:
Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] has the largest product 24.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # TODO: Implement your solution here
        pass


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    nums1 = [2, 3, -2, 4]
    print(f"Example 1 Result: {solution.maxProduct(nums1)} (Expected: 6)")

    # Example 2
    nums2 = [-2, 0, -1]
    print(f"Example 2 Result: {solution.maxProduct(nums2)} (Expected: 0)")

    # Example 3
    nums3 = [-2, 3, -4]
    print(f"Example 3 Result: {solution.maxProduct(nums3)} (Expected: 24)")
