from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array.

        Constraints:
            - n == nums.length
            - 1 <= n <= 10^4
            - 0 <= nums[i] <= n
            - All the numbers of nums are unique.
        """
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [3, 0, 1]
    print(f"Test 1: {sol.missingNumber(nums1)} (Expected: 2)")
    
    # Test Case 2
    nums2 = [0, 1]
    print(f"Test 2: {sol.missingNumber(nums2)} (Expected: 2)")
    
    # Test Case 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Test 3: {sol.missingNumber(nums3)} (Expected: 8)")
