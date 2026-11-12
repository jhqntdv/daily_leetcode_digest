class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Given a non-empty array of integers `nums`, every element appears twice except for one.
        Find that single element.

        You must implement a solution with a linear runtime complexity O(n) and use only constant extra space O(1).

        Constraints:
        - 1 <= nums.length <= 3 * 10^4
        - -3 * 10^4 <= nums[i] <= 3 * 10^4
        - Each element in the array appears twice except for one element which appears only once.
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [2, 2, 1]
    print(f"Test 1: nums = {nums1} -> Output: {sol.singleNumber(nums1)} (Expected: 1)")

    # Test Case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Test 2: nums = {nums2} -> Output: {sol.singleNumber(nums2)} (Expected: 4)")

    # Test Case 3
    nums3 = [1]
    print(f"Test 3: nums = {nums3} -> Output: {sol.singleNumber(nums3)} (Expected: 1)")
