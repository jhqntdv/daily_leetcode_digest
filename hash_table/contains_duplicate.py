class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

        Example 1:
        Input: nums = [1,2,3,1]
        Output: true

        Example 2:
        Input: nums = [1,2,3,4]
        Output: false

        Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

        Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        """
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}, Output: {sol.containsDuplicate(nums1)}") # Expected: True

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2}, Output: {sol.containsDuplicate(nums2)}") # Expected: False

    # Test Case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3}, Output: {sol.containsDuplicate(nums3)}") # Expected: True
