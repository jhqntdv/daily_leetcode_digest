from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.

        Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 10
        - -100 <= matrix[i][j] <= 100

        Approach (Four Shrinking Boundaries):
        - Maintain four boundaries: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
        - Repeatedly peel the outer layer in 4 directional sweeps while `top <= bottom and left <= right`:
            1. Traverse Right along `top` row (`left` -> `right`), then increment `top`.
            2. Traverse Down along `right` col (`top` -> `bottom`), then decrement `right`.
            3. If `top <= bottom`, traverse Left along `bottom` row (`right` -> `left`), then decrement `bottom`.
            4. If `left <= right`, traverse Up along `left` col (`bottom` -> `top`), then increment `left`.

        Complexity:
        - Time: O(m * n), visiting every cell exactly once.
        - Space: O(1) auxiliary space beyond the output list.
        """
        if not matrix or not matrix[0]:
            return []

        result: List[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Sweep right across top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # 2. Sweep down along right column
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # 3. Sweep left across bottom row (if a row remains)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # 4. Sweep up along left column (if a column remains)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Test Case 1 Output: {sol.spiralOrder(matrix1)}")
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test Case 2
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(f"Test Case 2 Output: {sol.spiralOrder(matrix2)}")
    # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # Test Case 3
    matrix3 = [[1]]
    print(f"Test Case 3 Output: {sol.spiralOrder(matrix3)}")
    # Expected: [1]
