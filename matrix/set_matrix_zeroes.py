"""
73. Set Matrix Zeroes
Difficulty: Medium

Given an m x n integer matrix 'matrix', if an element is 0, set its entire row and column to 0's.
You must do it in-place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Example 3:
Input: matrix = [[1,2,3],[4,0,6],[7,8,9]]
Output: [[1,0,3],[0,0,0],[7,8,9]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2**31 <= matrix[i][j] <= 2**31 - 1
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test case 1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix1)
    print(f"Test 1: {matrix1}")
    # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Test case 2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix2)
    print(f"Test 2: {matrix2}")
    # Expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # Test case 3
    matrix3 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    sol.setZeroes(matrix3)
    print(f"Test 3: {matrix3}")
    # Expected: [[1, 0, 3], [0, 0, 0], [7, 8, 9]]
