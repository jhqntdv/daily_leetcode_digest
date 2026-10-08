"""
Title: Container With Most Water
Difficulty: Medium
Tag: Two Pointers

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
the max area of water the container can contain is 49.

Example 2:
Input: height = [1, 1]
Output: 1

Example 3:
Input: height = [4, 3, 2, 1, 4]
Output: 16

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            h = min(height[l], height[r])
            max_water = max(max_water, (r - l) * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    t1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected1 = 49
    res1 = solution.maxArea(t1)
    print(f"Test 1: result={res1}, expected={expected1} -> {'PASS' if res1 == expected1 else 'FAIL'}")

    # Test Case 2
    t2 = [1, 1]
    expected2 = 1
    res2 = solution.maxArea(t2)
    print(f"Test 2: result={res2}, expected={expected2} -> {'PASS' if res2 == expected2 else 'FAIL'}")

    # Test Case 3
    t3 = [4, 3, 2, 1, 4]
    expected3 = 16
    res3 = solution.maxArea(t3)
    print(f"Test 3: result={res3}, expected={expected3} -> {'PASS' if res3 == expected3 else 'FAIL'}")
