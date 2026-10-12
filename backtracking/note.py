"""
# Algorithm Cheat Sheet: Backtracking

## Core Concepts & Guarantees:
Backtracking is a systematic method for exploring all possible configurations in a search space.
It constructs candidates to the solutions incrementally, and abandons a candidate ("backtracks")
as soon as it determines that the candidate cannot possibly lead to a valid solution.

A backtracking problem can always be modeled as a **Depth-First Search (DFS) on an implicit decision tree**:
1. **Choose**: Make a decision, update the current path and state.
2. **Explore**: Recurse down the tree to make further decisions.
3. **Unchoose (Backtrack)**: Revert the decision to restore the state before exploring other branches.

---

## Core Patterns:

1. **Subsets / Power Set**:
   - Every node in the recursion tree represents a valid state.
   - At each level, iterate from `start_index` to the end of the array to avoid duplicate subset sets.
   - Decision: include element `nums[i]`, recurse with `i + 1`, then pop.

2. **Combinations & Target Sum (with / without reuse)**:
   - Target reached -> record answer.
   - Early Pruning: Sort the array first! If `nums[i] > remaining_target`, break early out of the loop.
   - If elements can be reused unlimited times: recurse with `start_index = i`.
   - If elements cannot be reused: recurse with `start_index = i + 1`.

3. **Permutations**:
   - Order matters, so every branch considers all unused elements (start loop from index `0`).
   - Track chosen elements using a `visited` boolean array / set, or by in-place element swapping.

4. **Handling Duplicates in the Input (Deduplication Pattern)**:
   - When input contains duplicates (e.g., `[1, 2, 2]`) and solutions must be unique:
     1. Sort the input array first: `nums.sort()`.
     2. Skip identical elements at the **same tree depth**:
        `if i > start and nums[i] == nums[i - 1]: continue`
     - Note: `i > start` ensures we allow duplicate values across different depths (e.g., using both 2s in `[2, 2]`),
       but prevent choosing the second '2' as the same sibling choice at the current level.

5. **Grid / Graph Constraint Search (Word Search, N-Queens, Sudoku)**:
   - State representation often includes board state or visited coordinates `(r, c)`.
   - Temporarily modify the grid (e.g., `board[r][c] = '#'`) and restore on backtrack (`board[r][c] = char`).
   - Return a boolean (`True`/`False`) if only searching for an existential solution, or accumulate into a list if collecting all configurations.

---

## Common Pitfalls & Edge Cases:
- **Shallow Copy Bug**: Appending `path` directly to `res` (e.g., `res.append(path)`) stores references.
  When `path` is modified or popped, all stored solutions mutate! Always use `res.append(list(path))` or `res.append(path[:])`.
- **Forgetting to Backtrack**: Missing `path.pop()` or failing to reset visited flags leads to incorrect branch exploration.
- **Deduplication Check Condition**: Checking `nums[i] == nums[i - 1]` without `i > start` will mistakenly prune valid vertical branches (parent-child).
- **Pruning Pre-condition**: Loop-break pruning (`if val > remain: break`) requires the candidates array to be sorted first.
- **Python Recursion Limit**: Python's default recursion limit is 1000. For deep trees, use iterative methods or increase `sys.setrecursionlimit`.
"""

from typing import List


def template_subsets(nums: List[int]) -> List[List[int]]:
    """
    Pattern: Subsets / Power Set
    Generates all 2^n subsets of unique elements.
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    """
    res: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        res.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res


def template_combinations_k(n: int, k: int) -> List[List[int]]:
    """
    Pattern: Combinations of size k from numbers 1 to n.
    Includes size-based pruning (stop if remaining elements aren't enough to reach k).
    Time Complexity: O(k * C(n, k))
    Space Complexity: O(k)
    """
    res: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        if len(path) == k:
            res.append(list(path))
            return

        # Pruning: need (k - len(path)) more elements.
        # Max start index we can pick is n - (k - len(path)) + 1
        max_start = n - (k - len(path)) + 1
        for i in range(start, max_start + 1):
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return res


def template_permutations(nums: List[int]) -> List[List[int]]:
    """
    Pattern: Permutations of distinct numbers.
    Explores all orders using a boolean used array.
    Time Complexity: O(n * n!)
    Space Complexity: O(n)
    """
    res: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            res.append(list(path))
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res


def template_deduplication(nums: List[int]) -> List[List[int]]:
    """
    Pattern: Deduplication with duplicate input elements (e.g., Subsets II).
    Requires sorting and skipping sibling duplicates.
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    """
    nums.sort()
    res: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        res.append(list(path))
        for i in range(start, len(nums)):
            # Skip sibling duplicates at the same tree depth
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res
