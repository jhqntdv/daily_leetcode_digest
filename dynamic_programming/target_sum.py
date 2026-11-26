from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        You are given an integer array nums and an integer target.

        You want to build an expression out of nums by adding one of the symbols '+' and '-'
        before each integer in nums and then concatenate all the integers.

        Return the number of different expressions that you can build, which evaluates to target.

        Constraints:
        - 1 <= nums.length <= 20
        - 0 <= nums[i] <= 1000
        - 0 <= sum(nums[i]) <= 1000
        - -1000 <= target <= 1000
        """
        # Write your solution here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1, target1 = [1, 1, 1, 1, 1], 3
    print(f"Test Case 1: nums = {nums1}, target = {target1}")
    print(f"Output: {sol.findTargetSumWays(nums1, target1)} | Expected: 5\n")
    
    # Test Case 2
    nums2, target2 = [1], 1
    print(f"Test Case 2: nums = {nums2}, target = {target2}")
    print(f"Output: {sol.findTargetSumWays(nums2, target2)} | Expected: 1\n")
    
    # Test Case 3
    nums3, target3 = [1, 2, 1], 0
    print(f"Test Case 3: nums = {nums3}, target = {target3}")
    print(f"Output: {sol.findTargetSumWays(nums3, target3)} | Expected: 2\n")
