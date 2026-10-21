"""
Title: Unique Paths
Difficulty: Medium
Tag: dynamic_programming

Problem Statement:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach
the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Examples:
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 3, n = 3
Output: 6

Constraints:
- 1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    m1, n1 = 3, 7
    expected1 = 28
    result1 = solution.uniquePaths(m1, n1)
    print(f"Test 1: {'PASSED' if result1 == expected1 else 'FAILED'} (Got: {result1}, Expected: {expected1})")

    # Test Case 2
    m2, n2 = 3, 2
    expected2 = 3
    result2 = solution.uniquePaths(m2, n2)
    print(f"Test 2: {'PASSED' if result2 == expected2 else 'FAILED'} (Got: {result2}, Expected: {expected2})")

    # Test Case 3
    m3, n3 = 3, 3
    expected3 = 6
    result3 = solution.uniquePaths(m3, n3)
    print(f"Test 3: {'PASSED' if result3 == expected3 else 'FAILED'} (Got: {result3}, Expected: {expected3})")
