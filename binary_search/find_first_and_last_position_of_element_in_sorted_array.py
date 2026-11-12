from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in non-decreasing order,
        find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.
        """
        # Write your code here
        pass

if __name__ == '__main__':
    solution = Solution()
    
    # Example 1
    nums1, target1 = [5, 7, 7, 8, 8, 10], 8
    print(f"Example 1: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.searchRange(nums1, target1)}")
    print(f"Expected: [3, 4]\n")
    
    # Example 2
    nums2, target2 = [5, 7, 7, 8, 8, 10], 6
    print(f"Example 2: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.searchRange(nums2, target2)}")
    print(f"Expected: [-1, -1]\n")
    
    # Example 3
    nums3, target3 = [], 0
    print(f"Example 3: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.searchRange(nums3, target3)}")
    print(f"Expected: [-1, -1]\n")
