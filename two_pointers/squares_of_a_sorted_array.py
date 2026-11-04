class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums sorted in non-decreasing order,
        return an array of the squares of each number sorted in non-decreasing order.
        """
        # Your code here
        pass

if __name__ == '__main__':
    sol = Solution()

    # Example 1
    nums1 = [-4, -1, 0, 3, 10]
    expected1 = [0, 1, 9, 16, 100]
    result1 = sol.sortedSquares(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}, Pass: {result1 == expected1}")

    # Example 2
    nums2 = [-7, -3, 2, 3, 11]
    expected2 = [4, 9, 9, 49, 121]
    result2 = sol.sortedSquares(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}, Pass: {result2 == expected2}")

    # Example 3
    nums3 = [-5, -3, -2, -1]
    expected3 = [1, 4, 9, 25]
    result3 = sol.sortedSquares(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}, Pass: {result3 == expected3}")