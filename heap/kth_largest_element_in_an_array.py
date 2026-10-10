"""
Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Can you solve it without sorting in O(n log k) or average O(n) time complexity?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Example 3:
Input: nums = [7,10,4,3,20,15], k = 3
Output: 10

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test case 1
    nums1, k1 = [3, 2, 1, 5, 6, 4], 2
    res1 = sol.findKthLargest(nums1, k1)
    print(f"Test 1: Expected 5, Got {res1}")
    
    # Test case 2
    nums2, k2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    res2 = sol.findKthLargest(nums2, k2)
    print(f"Test 2: Expected 4, Got {res2}")
    
    # Test case 3
    nums3, k3 = [7, 10, 4, 3, 20, 15], 3
    res3 = sol.findKthLargest(nums3, k3)
    print(f"Test 3: Expected 10, Got {res3}")
