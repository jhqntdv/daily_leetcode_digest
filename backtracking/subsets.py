"""
Title: Subsets
Difficulty: Medium
Tag: Backtracking / Array

Problem Statement:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
Input: nums = [0]
Output: [[], [0]]

Example 3:
Input: nums = [1, 2]
Output: [[], [1], [2], [1, 2]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking approach:
        Every node in the recursion tree represents a valid subset. We add the
        current path to results at each step, and explore choices starting from
        the current index onwards to prevent duplicate subsets.

        Time Complexity: O(n * 2^n) - There are 2^n subsets, and copying each takes O(n).
        Space Complexity: O(n) - Maximum recursion stack depth is n.
        """
        res: List[List[int]] = []
        path: List[int] = []

        def backtrack(start_index: int) -> None:
            # Every node in the recursion tree corresponds to a valid subset
            res.append(list(path))

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3]
    res1 = sol.subsets(nums1)
    print(f"Test 1 Input: {nums1}")
    print(f"Test 1 Output: {res1}")
    print(f"Test 1 Count: {len(res1)} (Expected: 8)\n")

    # Test Case 2
    nums2 = [0]
    res2 = sol.subsets(nums2)
    print(f"Test 2 Input: {nums2}")
    print(f"Test 2 Output: {res2}")
    print(f"Test 2 Count: {len(res2)} (Expected: 2)\n")

    # Test Case 3
    nums3 = [1, 2]
    res3 = sol.subsets(nums3)
    print(f"Test 3 Input: {nums3}")
    print(f"Test 3 Output: {res3}")
    print(f"Test 3 Count: {len(res3)} (Expected: 4)\n")
