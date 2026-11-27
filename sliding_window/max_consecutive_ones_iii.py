from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Given a binary array `nums` and an integer `k`, return the maximum number
        of consecutive 1's in the array if you can flip at most `k` 0's.

        Constraints:
        - 1 <= nums.length <= 10^5
        - nums[i] is either 0 or 1.
        - 0 <= k <= nums.length
        """
        # Write your solution here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k1 = 2
    print(f"Example 1 Output: {sol.longestOnes(nums1, k1)} | Expected: 6")
    
    # Test Case 2
    nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k2 = 3
    print(f"Example 2 Output: {sol.longestOnes(nums2, k2)} | Expected: 10")
    
    # Test Case 3
    nums3 = [0, 0, 0, 1]
    k3 = 4
    print(f"Example 3 Output: {sol.longestOnes(nums3, k3)} | Expected: 4")
