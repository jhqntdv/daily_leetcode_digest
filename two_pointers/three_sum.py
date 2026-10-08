from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        
        Notice that the solution set must not contain duplicate triplets.
        
        Constraints:
            - 3 <= nums.length <= 3000
            - -10^5 <= nums[i] <= 10^5
        """
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Test Case 1: nums = {nums1}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]] (order may vary)")
    print(f"Output:   {sol.threeSum(nums1)}")
    print("-" * 50)
    
    # Test case 2
    nums2 = [0, 1, 1]
    print(f"Test Case 2: nums = {nums2}")
    print(f"Expected: []")
    print(f"Output:   {sol.threeSum(nums2)}")
    print("-" * 50)
    
    # Test case 3
    nums3 = [0, 0, 0]
    print(f"Test Case 3: nums = {nums3}")
    print(f"Expected: [[0, 0, 0]]")
    print(f"Output:   {sol.threeSum(nums3)}")
    print("-" * 50)
