"""
Two Sum (Easy)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = dict()
        for i, num in enumerate(nums):
            if target - num in mp:
                return [mp[target - num], i]
            mp[num] = i
        return []

if __name__ == '__main__':
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1 - Expected: [0, 1], Got: {solution.twoSum(nums1, target1)}")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2 - Expected: [1, 2], Got: {solution.twoSum(nums2, target2)}")
