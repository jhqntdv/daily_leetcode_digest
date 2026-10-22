from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Title: Rotting Oranges
        Difficulty: Medium
        Tag: Graph / Breadth-First Search

        Problem Statement:
        You are given an m x n grid where each cell can have one of three values:
        - 0 representing an empty cell,
        - 1 representing a fresh orange, or
        - 2 representing a rotten orange.

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.
        If this is impossible, return -1.

        Example 1:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

        Example 2:
        Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

        Example 3:
        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

        Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 10
        - grid[i][j] is 0, 1, or 2.

        Complexity:
        Time Complexity: O(m * n) - each cell is visited at most once.
        Space Complexity: O(m * n) - queue can hold all rotten cells in the worst case.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Collect all initial rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges from the start, 0 minutes are needed
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # Step 2: Multi-source BFS layer by layer (each layer = 1 minute)
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes if fresh_count == 0 else -1


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(f"Test 1 Output: {solution.orangesRotting(grid1)} | Expected: 4")

    # Test Case 2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(f"Test 2 Output: {solution.orangesRotting(grid2)} | Expected: -1")

    # Test Case 3
    grid3 = [[0,2]]
    print(f"Test 3 Output: {solution.orangesRotting(grid3)} | Expected: 0")
