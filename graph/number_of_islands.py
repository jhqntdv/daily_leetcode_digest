from typing import List

class Solution:
    """
    Title: Number of Islands
    Difficulty: Medium

    Problem Statement:
    Given an m x n 2D binary grid `grid` which represents a map of '1's (land)
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are all
    surrounded by water.

    Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

    Example 3:
    Input: grid = [
      ["1","0","1","1","0","1","1"]
    ]
    Output: 3

    Constraints:
    - m == len(grid)
    - n == len(grid[i])
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # Write your code here
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected1 = 1
    actual1 = solution.numIslands([row[:] for row in grid1])
    print(f"Test Case 1: Expected={expected1}, Got={actual1}")

    # Test Case 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    expected2 = 3
    actual2 = solution.numIslands([row[:] for row in grid2])
    print(f"Test Case 2: Expected={expected2}, Got={actual2}")

    # Test Case 3
    grid3 = [
        ["1", "0", "1", "1", "0", "1", "1"],
    ]
    expected3 = 3
    actual3 = solution.numIslands([row[:] for row in grid3])
    print(f"Test Case 3: Expected={expected3}, Got={actual3}")
