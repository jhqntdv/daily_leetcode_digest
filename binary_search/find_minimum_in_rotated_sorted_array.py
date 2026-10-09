from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        For example, the array nums = [0,1,2,4,5,6,7] might become:
        - [4,5,6,7,0,1,2] if it was rotated 4 times.
        - [0,1,2,4,5,6,7] if it was rotated 7 times.

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        Constraints:
        - n == nums.length
        - 1 <= n <= 5000
        - -5000 <= nums[i] <= 5000
        - All the integers of nums are unique.
        - nums is sorted and rotated between 1 and n times.
        """
        # Write your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [3, 4, 5, 1, 2]
    print(f"Test Case 1: {nums1} -> Expected: 1, Got: {sol.findMin(nums1)}")
    
    # Test Case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Test Case 2: {nums2} -> Expected: 0, Got: {sol.findMin(nums2)}")
    
    # Test Case 3
    nums3 = [11, 13, 15, 17]
    print(f"Test Case 3: {nums3} -> Expected: 11, Got: {sol.findMin(nums3)}")
