from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
        This matrix has the following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the previous row.

        Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 100
        - -10^4 <= matrix[i][j], target <= 10^4

        Approach (Virtual 1D Array Binary Search):
        - Because each row is sorted and the first element of row i is greater than the last
          element of row i-1, the entire m x n matrix is equivalent to a strictly sorted 1D
          array of length m * n.
        - A 1D index `idx` in [0, m * n - 1] maps to 2D coordinates:
            row = idx // n
            col = idx % n
        - Run standard binary search over [0, m * n - 1].

        Complexity:
        - Time: O(log(m * n)) = O(log m + log n)
        - Space: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == '__main__':
    sol = Solution()

    # Test case 1
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    print(f"Test 1: {sol.searchMatrix(matrix1, target1)} (Expected: True)")

    # Test case 2
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    print(f"Test 2: {sol.searchMatrix(matrix2, target2)} (Expected: False)")

    # Test case 3
    matrix3 = [[1]]
    target3 = 1
    print(f"Test 3: {sol.searchMatrix(matrix3, target3)} (Expected: True)")
