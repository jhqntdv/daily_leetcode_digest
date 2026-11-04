"""
# Algorithm Cheat Sheet: Matrix (2D Grid Manipulation)

## Core Patterns:

### 1. Four Shrinking Boundaries (Spiral Traversal)
- Maintain four inclusive pointers: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
- Peel the perimeter in 4 steps per loop:
  1. Left $\to$ Right along `top`; `top += 1`
  2. Top $\to$ Bottom along `right`; `right -= 1`
  3. **(Check `top <= bottom`)** Right $\to$ Left along `bottom`; `bottom -= 1`
  4. **(Check `left <= right`)** Bottom $\to$ Top along `left`; `left += 1`
- The inner checks in steps 3 and 4 prevent duplicate traversal on non-square single-row or single-column remnants!

### 2. First Row & First Column as In-Place State Markers (Set Matrix Zeroes)
- To avoid $O(m + n)$ extra boolean arrays when marking rows/columns:
  1. Record `first_row_has_zero` and `first_col_has_zero` in two boolean variables.
  2. Use `matrix[r][0]` and `matrix[0][c]` as flags for interior cells `r >= 1, c >= 1`.
  3. Update interior cells based on the first row/column flags.
  4. Update the first row and first column last using the two boolean variables.
- Achieves $O(m \cdot n)$ time and $O(1)$ space.

### 3. In-Place Matrix Transpose & Rotation (Rotate Image $90^\circ$)
- **Clockwise $90^\circ$ Rotation**:
  1. **Transpose** across main diagonal: swap `matrix[r][c]` with `matrix[c][r]` for `r < c`.
  2. **Reverse each row**: `row.reverse()`.
- **Counter-Clockwise $90^\circ$ Rotation**:
  1. **Transpose** across main diagonal.
  2. **Reverse each column** (or reverse rows first, then transpose).

---

## Common Pitfalls & Edge Cases:
- **Overwriting `matrix[0][0]` in Set Matrix Zeroes**:
  - `matrix[0][0]` belongs to both the first row and the first column. Using separate `first_row_zero` and `first_col_zero` booleans avoids ambiguity.
- **Duplicate Row/Col Read in Spiral Order**:
  - For a $1 \times 4$ matrix, step 1 reads the row and increments `top` past `bottom`. Without `if top <= bottom:` before step 3, step 3 would read the same row backward!
- **Swapping Twice in Transpose**:
  - Iterate `for r in range(n): for c in range(r + 1, n):`. Iterating `c` from `0` to `n` swaps every pair twice, returning the original matrix.
"""

from typing import List


# ============================================================================
# Template 1: Spiral Matrix Traversal (4 Shrinking Boundaries)
# ============================================================================
def template_spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Returns all elements of an m x n matrix in clockwise spiral order.
    Time: O(m * n), Space: O(1) extra
    """
    if not matrix or not matrix[0]:
        return []
    res: List[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res


# ============================================================================
# Template 2: Rotate N x N Matrix 90 Degrees Clockwise In-Place
# ============================================================================
def template_rotate_90_clockwise(matrix: List[List[int]]) -> None:
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in-place.
    Time: O(n^2), Space: O(1)
    """
    n = len(matrix)
    # 1. Transpose across main diagonal
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    # 2. Reverse each row
    for row in matrix:
        row.reverse()

