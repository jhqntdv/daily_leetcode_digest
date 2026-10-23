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
        """
        # TODO: Implement your solution here
        pass

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
