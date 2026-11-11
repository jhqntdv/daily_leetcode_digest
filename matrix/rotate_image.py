"""
48. Rotate Image
Difficulty: Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(m1)
    print(f"Test 1: {m1}")
    assert m1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test Case 2
    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(m2)
    print(f"Test 2: {m2}")
    assert m2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # Test Case 3
    m3 = [[1]]
    solution.rotate(m3)
    print(f"Test 3: {m3}")
    assert m3 == [[1]]

    print("All test cases passed!")
