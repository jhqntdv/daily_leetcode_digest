"""
Title: Surrounded Regions
Difficulty: Medium
LeetCode: 130

Problem Statement:
Given an m x n matrix 'board' containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
Any 'O' on the boundary, or connected 4-directionally to an 'O' on the boundary, cannot be surrounded and will not be flipped.

Examples:
Example 1:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped. The other three 'O's are surrounded and flipped to 'X'.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Example 3:
Input: board = [
  ["O","X","X"],
  ["X","O","X"],
  ["X","X","O"]
]
Output: [
  ["O","X","X"],
  ["X","X","X"],
  ["X","X","O"]
]

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board1)
    expected1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    assert board1 == expected1, f"Test 1 Failed: {board1}"

    # Test Case 2
    board2 = [["X"]]
    solution.solve(board2)
    expected2 = [["X"]]
    assert board2 == expected2, f"Test 2 Failed: {board2}"

    # Test Case 3
    board3 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "O"]
    ]
    solution.solve(board3)
    expected3 = [
        ["O", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "O"]
    ]
    assert board3 == expected3, f"Test 3 Failed: {board3}"

    print("All test cases passed!")
