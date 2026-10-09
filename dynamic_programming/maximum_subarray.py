from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        Constraints:
        - 1 <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
        """
        # Write your solution here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Test Case 1: {sol.maxSubArray(nums1)} (Expected: 6)")
    
    # Test Case 2
    nums2 = [1]
    print(f"Test Case 2: {sol.maxSubArray(nums2)} (Expected: 1)")
    
    # Test Case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"Test Case 3: {sol.maxSubArray(nums3)} (Expected: 23)")
