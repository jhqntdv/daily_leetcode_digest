class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Given a sorted array `nums`, remove the duplicates in-place such that each unique
        element appears only once. The relative order of the elements should be kept
        the same. Then return the new length.

        Do not allocate extra space for another array. You must do this by modifying
        the input array in-place with O(1) extra memory.

        The judge will test your solution with the following code:

        ```python
        nums = [...] # Input array
        expected_nums = [...] # The expected answer with correct length

        k = Solution().removeDuplicates(nums) # Calls your implementation

        assert k == len(expected_nums)
        for i in range(k):
            assert nums[i] == expected_nums[i]
        ```

        If all assertions pass, then your solution will be accepted.

        Examples:
        1. Input: nums = [1,1,2]
           Output: 2, nums = [1,2,_]
           Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
           It does not matter what you leave beyond the returned k (hence they are underscores).

        2. Input: nums = [0,0,1,1,1,2,2,3,3,4]
           Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
           Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
           It does not matter what you leave beyond the returned k.

        3. Input: nums = []
           Output: 0, nums = []
           Explanation: An empty array should result in a length of 0.

        Constraints:
        - 0 <= nums.length <= 3 * 10^4
        - -100 <= nums[i] <= 100
        - nums is sorted in non-decreasing order.
        """
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [1, 1, 2]
    expected_nums1 = [1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"Test Case 1: Input: {nums1[:len(expected_nums1)]}, Expected k: {len(expected_nums1)}, Actual k: {k1}")
    assert k1 == len(expected_nums1)
    for i in range(k1):
        assert nums1[i] == expected_nums1[i]
    print("Test Case 1 passed!")

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums2 = [0, 1, 2, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"Test Case 2: Input: {nums2[:len(expected_nums2)]}, Expected k: {len(expected_nums2)}, Actual k: {k2}")
    assert k2 == len(expected_nums2)
    for i in range(k2):
        assert nums2[i] == expected_nums2[i]
    print("Test Case 2 passed!")

    # Test Case 3
    nums3 = []
    expected_nums3 = []
    k3 = sol.removeDuplicates(nums3)
    print(f"Test Case 3: Input: {nums3[:len(expected_nums3)]}, Expected k: {len(expected_nums3)}, Actual k: {k3}")
    assert k3 == len(expected_nums3)
    for i in range(k3):
        assert nums3[i] == expected_nums3[i]
    print("Test Case 3 passed!")
