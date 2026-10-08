class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums of length n where all the integers of nums are in the range [1, n]
        and each integer appears once or twice, return an array of all the integers that appear twice.

        You must write an algorithm that runs in O(n) time and uses only constant extra space.

        Example 1:
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [2,3]

        Example 2:
        Input: nums = [1,1,2]
        Output: [1]

        Example 3:
        Input: nums = [1]
        Output: []

        Constraints:
        n == nums.length
        1 <= n <= 10^5
        1 <= nums[i] <= n
        Each element in nums appears once or twice.
        """
        duplicates = []
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] < 0:
                duplicates.append(abs(x))
            else:
                nums[idx] = -nums[idx]
        return duplicates

if __name__ == '__main__':
    s = Solution()

    # Test Case 1
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    expected1 = [2, 3]
    result1 = s.findDuplicates(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}")
    assert sorted(result1) == sorted(expected1), f"Test Case 1 Failed: Expected {expected1}, Got {result1}"

    # Test Case 2
    nums2 = [1, 1, 2]
    expected2 = [1]
    result2 = s.findDuplicates(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}")
    assert sorted(result2) == sorted(expected2), f"Test Case 2 Failed: Expected {expected2}, Got {result2}"

    # Test Case 3
    nums3 = [1]
    expected3 = []
    result3 = s.findDuplicates(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}")
    assert sorted(result3) == sorted(expected3), f"Test Case 3 Failed: Expected {expected3}, Got {result3}"

    print("All test cases passed!")
