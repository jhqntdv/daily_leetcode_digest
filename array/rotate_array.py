from typing import List

class Solution:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Modify nums in-place.

    Examples:
    Example 1:
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
        Input: nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation:
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]

    Example 3:
        Input: nums = [1,2], k = 3
        Output: [2,1]

    Constraints:
        - 1 <= nums.length <= 10^5
        - -2^31 <= nums[i] <= 2^31 - 1
        - 0 <= k <= 10^5
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    print(f"Test 1 Output: {nums1}")
    assert nums1 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5, 6, 7, 1, 2, 3, 4], got {nums1}"

    # Test 2
    nums2 = [-1, -100, 3, 99]
    sol.rotate(nums2, 2)
    print(f"Test 2 Output: {nums2}")
    assert nums2 == [3, 99, -1, -100], f"Expected [3, 99, -1, -100], got {nums2}"

    # Test 3
    nums3 = [1, 2]
    sol.rotate(nums3, 3)
    print(f"Test 3 Output: {nums3}")
    assert nums3 == [2, 1], f"Expected [2, 1], got {nums3}"

    print("All tests passed!")
