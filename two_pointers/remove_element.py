class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements that are not equal to val may be changed. Then return the number of
        elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k. To be accepted,
        you need to return k.

        The judge will test your solution with the following code:
        int[] nums = [...]; // Input array
        int val = ...; // Value to remove
        int[] expectedNums = [...]; // The expected answer with correct length.
                                    // It is sorted with no instances of val.

        int k = removeElement(nums, val); // Calls your implementation

        assert k == expectedNums.length;
        sort(nums, 0, k); // Sort the first k elements of nums
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }

        It does not matter what you leave beyond the first k elements.

        Example 1:
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
                     It does not matter what you leave beyond the returned k (hence they are underscores).

        Example 2:
        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        Explanation: Your function should return k = 5, with the first five elements of nums containing
                     0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary.
                     It does not matter what you leave beyond the returned k (hence they are underscores).

        Example 3:
        Input: nums = [1], val = 1
        Output: 0, nums = []
        Explanation: Your function should return k = 0, with the array being empty.

        Constraints:
        0 <= nums.length <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100
        """
        # Your code here
        pass

if __name__ == '__main__':
    s = Solution()

    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = s.removeElement(nums1, val1)
    print(f"Input: nums = {nums1[:len(nums1)]}, val = {val1}")
    print(f"Output: k = {k1}, nums = {nums1[:k1]}") # The actual content beyond k is irrelevant
    assert k1 == 2 and sorted(nums1[:k1]) == [2, 2], f"Test 1 Failed: Expected k=2, nums=[2,2], Got k={k1}, nums={nums1[:k1]}"
    print("Test 1 Passed\n")

    # Example 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = s.removeElement(nums2, val2)
    print(f"Input: nums = {nums2[:len(nums2)]}, val = {val2}")
    print(f"Output: k = {k2}, nums = {nums2[:k2]}")
    assert k2 == 5 and sorted(nums2[:k2]) == [0, 0, 1, 3, 4], f"Test 2 Failed: Expected k=5, nums in any order, Got k={k2}, nums={nums2[:k2]}"
    print("Test 2 Passed\n")

    # Example 3
    nums3 = [1]
    val3 = 1
    k3 = s.removeElement(nums3, val3)
    print(f"Input: nums = {nums3[:len(nums3)]}, val = {val3}")
    print(f"Output: k = {k3}, nums = {nums3[:k3]}")
    assert k3 == 0 and nums3[:k3] == [], f"Test 3 Failed: Expected k=0, nums=[], Got k={k3}, nums={nums3[:k3]}"
    print("Test 3 Passed\n")
