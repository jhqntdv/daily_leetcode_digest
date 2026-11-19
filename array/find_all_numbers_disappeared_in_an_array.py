class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n],
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Example 1:
        Input: nums = [4,3,2,7,8,2,3,1]
        Output: [5,6]

        Example 2:
        Input: nums = [1,1]
        Output: [2]

        Example 3:
        Input: nums = [1,2,3,4]
        Output: []

        Constraints:
        n == nums.length
        1 <= n <= 10^5
        1 <= nums[i] <= n
        """
        # Your code here
        pass

if __name__ == '__main__':
    sol = Solution()

    # Example 1
    nums1 = [4,3,2,7,8,2,3,1]
    expected1 = [5,6]
    result1 = sol.findDisappearedNumbers(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}")
    assert sorted(result1) == sorted(expected1), f"Test 1 Failed: Expected {expected1}, Got {result1}"

    # Example 2
    nums2 = [1,1]
    expected2 = [2]
    result2 = sol.findDisappearedNumbers(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}")
    assert sorted(result2) == sorted(expected2), f"Test 2 Failed: Expected {expected2}, Got {result2}"

    # Example 3
    nums3 = [1,2,3,4]
    expected3 = []
    result3 = sol.findDisappearedNumbers(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}")
    assert sorted(result3) == sorted(expected3), f"Test 3 Failed: Expected {expected3}, Got {result3}"

    print("\nAll test cases passed!")
