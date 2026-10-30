class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. 
        You can return the answer in any order.

        Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        Example 2:
        Input: nums = [0,1]
        Output: [[0,1],[1,0]]

        Example 3:
        Input: nums = [1]
        Output: [[1]]

        Constraints:
        - 1 <= nums.length <= 6
        - -10 <= nums[i] <= 10
        - All the integers of nums are unique.
        """
        # TODO: Implement solution
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {sol.permute(nums1)}\n")

    # Test Case 2
    nums2 = [0, 1]
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {sol.permute(nums2)}\n")

    # Test Case 3
    nums3 = [1]
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {sol.permute(nums3)}\n")
