"""
Word Search (LeetCode #79)
Difficulty: Medium

Given an m x n grid of characters 'board' and a string 'word', return true if 'word' exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: True

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: False

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consist of only lowercase and uppercase English letters.
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    print(f"Test 1: {sol.exist(board1, word1)} (Expected: True)")

    # Test Case 2
    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"
    print(f"Test 2: {sol.exist(board2, word2)} (Expected: True)")

    # Test Case 3
    board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCB"
    print(f"Test 3: {sol.exist(board3, word3)} (Expected: False)")
