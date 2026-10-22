from collections import deque
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
        """
        BFS Flood Fill:
        Iterate through every cell in the grid. When an unvisited land cell ('1') is encountered,
        increment the island count and trigger a BFS to sink (mark as '0') all connected land cells.

        Using BFS with a queue avoids Python's recursion depth limit on large grids (up to 300x300).

        Time Complexity: O(m * n) where m and n are grid dimensions.
        Space Complexity: O(min(m, n)) for the BFS queue in the worst case.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    # Sink the island starting at (r, c)
                    grid[r][c] = "0"
                    queue = deque([(r, c)])
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"  # Mark visited immediately upon enqueuing
                                queue.append((nr, nc))

        return island_count


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
