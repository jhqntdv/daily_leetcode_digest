class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain
        amount of money stashed, the only constraint stopping you from robbing each of them is that
        adjacent houses have security systems connected and it will automatically contact the police
        if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, return the maximum
        amount of money you can rob tonight without alerting the police.

        Constraints:
        - 1 <= nums.length <= 100
        - 0 <= nums[i] <= 400
        """
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Test 1: nums = {nums1} -> Output: {sol.rob(nums1)} (Expected: 4)")

    # Test Case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"Test 2: nums = {nums2} -> Output: {sol.rob(nums2)} (Expected: 12)")

    # Test Case 3
    nums3 = [2, 1, 1, 2]
    print(f"Test 3: nums = {nums3} -> Output: {sol.rob(nums3)} (Expected: 4)")
