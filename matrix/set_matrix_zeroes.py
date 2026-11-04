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

        Approach (First Row & First Column as In-Place Markers in O(1) Space):
        1. Check whether the first row (`first_row_zero`) or first column (`first_col_zero`)
           originally contains any zeros.
        2. Scan the interior submatrix (`r >= 1, c >= 1`): whenever `matrix[r][c] == 0`,
           mark its row and column headers: `matrix[r][0] = 0` and `matrix[0][c] = 0`.
        3. Zero out interior cells `(r, c)` where either `matrix[r][0] == 0` or `matrix[0][c] == 0`.
        4. Finally, zero out the first row and/or first column if `first_row_zero` or `first_col_zero` is True.

        Complexity:
        - Time: O(m * n)
        - Space: O(1) auxiliary space.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))

        # Use first row and column as markers for interior cells
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero out marked interior cells
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out first row and first column if needed
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0


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
