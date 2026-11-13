class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.
        """
        # Write your solution here
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    nums1 = [3, 2, 3]
    res1 = sol.majorityElement(nums1)
    print(f"Test 1 Output: {res1} | Expected: 3")

    # Test Case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    res2 = sol.majorityElement(nums2)
    print(f"Test 2 Output: {res2} | Expected: 2")

    # Test Case 3
    nums3 = [1, 1, 1, 2, 3, 4, 1, 1]
    res3 = sol.majorityElement(nums3)
    print(f"Test 3 Output: {res3} | Expected: 1")
