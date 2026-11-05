from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target, return the 
        minimal length of a contiguous subarray whose sum is greater than or equal to target. 
        If there is no such subarray, return 0 instead.
        """
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    target1, nums1 = 7, [2, 3, 1, 2, 4, 3]
    res1 = sol.minSubArrayLen(target1, nums1)
    print(f"Test 1: target = {target1}, nums = {nums1} -> Output: {res1} (Expected: 2)")
    
    # Test Case 2
    target2, nums2 = 4, [1, 4, 4]
    res2 = sol.minSubArrayLen(target2, nums2)
    print(f"Test 2: target = {target2}, nums = {nums2} -> Output: {res2} (Expected: 1)")
    
    # Test Case 3
    target3, nums3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    res3 = sol.minSubArrayLen(target3, nums3)
    print(f"Test 3: target = {target3}, nums = {nums3} -> Output: {res3} (Expected: 0)")
