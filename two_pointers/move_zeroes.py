from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end of it while maintaining
        the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Example 1:
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:
        Input: nums = [0]
        Output: [0]

        Example 3:
        Input: nums = [1]
        Output: [1]

        Constraints:
        1 <= nums.length <= 10^4
        -2^31 <= nums[i] <= 2^31 - 1
        """
        # Your code here
        pass


if __name__ == '__main__':
    s = Solution()

    # Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    print(f"Original: {nums1}")
    s.moveZeroes(nums1)
    print(f"Modified: {nums1}") # Expected: [1, 3, 12, 0, 0]
    print("---------------------")

    # Test Case 2
    nums2 = [0]
    print(f"Original: {nums2}")
    s.moveZeroes(nums2)
    print(f"Modified: {nums2}") # Expected: [0]
    print("---------------------")

    # Test Case 3
    nums3 = [1]
    print(f"Original: {nums3}")
    s.moveZeroes(nums3)
    print(f"Modified: {nums3}") # Expected: [1]
    print("---------------------")

    # Additional Test Case
    nums4 = [0, 0, 1]
    print(f"Original: {nums4}")
    s.moveZeroes(nums4)
    print(f"Modified: {nums4}") # Expected: [1, 0, 0]
    print("---------------------")

    # Additional Test Case
    nums5 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    print(f"Original: {nums5}")
    s.moveZeroes(nums5)
    print(f"Modified: {nums5}") # Expected: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    print("---------------------")
