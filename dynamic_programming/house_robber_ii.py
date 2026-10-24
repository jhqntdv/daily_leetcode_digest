from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house has a
        certain amount of money stashed. All houses at this place are arranged in a circle.
        That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
        have a security system connected, and it will automatically contact the police if two
        adjacent houses on the same night were broken into.

        Given an integer array nums representing the amount of money of each house, return the
        maximum amount of money you can rob tonight without alerting the police.

        Examples:
        - Example 1: nums = [2, 3, 2] -> 3
        - Example 2: nums = [1, 2, 3, 1] -> 4
        - Example 3: nums = [1, 2, 3] -> 3

        Constraints:
        - 1 <= nums.length <= 1000
        - 0 <= nums[i] <= 1000
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [2, 3, 2]
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {sol.rob(nums1)} (Expected: 3)\n")

    # Test case 2
    nums2 = [1, 2, 3, 1]
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {sol.rob(nums2)} (Expected: 4)\n")

    # Test case 3
    nums3 = [1, 2, 3]
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {sol.rob(nums3)} (Expected: 3)\n")
