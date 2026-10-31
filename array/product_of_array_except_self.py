from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] 
        is equal to the product of all the elements of nums except nums[i].
        
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Constraints:
        - 2 <= nums.length <= 10^5
        - -30 <= nums[i] <= 30
        - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        
        Follow up: Can you solve the problem in O(1) extra space complexity? 
        (The output array does not count as extra space for space complexity analysis.)

        Approach (Two-Pass Prefix & Suffix Products in O(1) Extra Space):
        - For each index `i`, `answer[i]` is the product of all elements to the left of `i`
          multiplied by the product of all elements to the right of `i`.
        - Pass 1 (Left-to-Right): Store the running prefix product of `nums[0..i-1]` in `answer[i]`.
        - Pass 2 (Right-to-Left): Maintain a running scalar `suffix` product of `nums[i+1..n-1]`
          and multiply it directly into `answer[i]`.

        Complexity:
        - Time: O(n), two linear passes over the array.
        - Space: O(1) extra space (excluding the output array `answer`).
        """
        n = len(nums)
        answer = [1] * n

        # Pass 1: Prefix products (left to right)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: Suffix products (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(f"Test Case 1: nums = {nums1}")
    print("Expected: [24, 12, 8, 6]")
    print(f"Result:   {sol.productExceptSelf(nums1)}\n")
    
    # Test Case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Test Case 2: nums = {nums2}")
    print("Expected: [0, 0, 9, 0, 0]")
    print(f"Result:   {sol.productExceptSelf(nums2)}\n")
    
    # Test Case 3
    nums3 = [4, 5, 1, 8, 2]
    print(f"Test Case 3: nums = {nums3}")
    print("Expected: [80, 64, 320, 40, 160]")
    print(f"Result:   {sol.productExceptSelf(nums3)}\n")
