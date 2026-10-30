"""
# Algorithm Cheat Sheet: Binary Search

## Core Concepts & Guarantees:
Binary Search eliminates half of the search space at every step by exploiting **monotonicity**
(sorted order or a boolean condition that transitions from `False` to `True` once).
- **Time Complexity**: $O(\log N)$ where $N$ is the size of the search space.
- **Space Complexity**: $O(1)$ iterative.

---

## Two Fundamental Loop Templates:

### 1. Exact Match Lookup (`while left <= right`)
- **Use When**: You can determine whether `mid` is the final answer immediately without comparing to neighbors,
  and you want the search space to empty completely if not found.
- **Updates**: `left = mid + 1` or `right = mid - 1`.
- **Termination**: Terminates when `left > right` (empty interval).

### 2. Boundary / Minimum Feasible Search (`while left < right`)
- **Use When**: Searching for a transition boundary (e.g., first `True` in `[False, False, True, True]`,
  minimum in rotated array, or binary search on answer space).
- **Updates**:
  - If `mid` is feasible (could be the optimal answer): `right = mid` (keep `mid` in range).
  - If `mid` is not feasible: `left = mid + 1`.
- **Termination**: Terminates when `left == right`, converging on the exact boundary index.

---

## Core Algorithmic Patterns:

### Pattern 1: Lower Bound & Upper Bound (`bisect_left` / `bisect_right`)
- **Lower Bound (`bisect_left`)**: First index `i` where `nums[i] >= target`.
- **Upper Bound (`bisect_right`)**: First index `i` where `nums[i] > target`.
- **Count of `target` in sorted array**: `bisect_right(nums, target) - bisect_left(nums, target)`.

### Pattern 2: Rotated Sorted Array
- **Property 1 (Half-Sorted Invariant)**: Splitting a rotated sorted array at `mid` guarantees that at least
  one half (`[left..mid]` or `[mid..right]`) is strictly sorted.
  - Check `if nums[left] <= nums[mid]:` (left half sorted) vs `else:` (right half sorted).
  - Then check if `target` lies within the sorted half's endpoints.
- **Property 2 (Find Minimum / Pivot)**:
  - Compare `nums[mid]` against `nums[right]` (not `nums[left]`!):
  - If `nums[mid] > nums[right]`, the minimum is in `[mid + 1 .. right]`.
  - Else, the minimum is in `[left .. mid]`.

### Pattern 3: Binary Search on the Answer Space (Parametric Search)
- **Use When**: Problem asks for the "minimum possible maximum" or "maximum possible minimum"
  (e.g., Koko Eating Bananas, Capacity to Ship Packages, Split Array Largest Sum).
- **Steps**:
  1. Identify the range of possible answers `[low, high]`.
  2. Define a monotonic feasibility function `can_achieve(x) -> bool`.
  3. Binary search for the smallest `x` where `can_achieve(x)` is `True`.

### Pattern 4: 2D Matrix Binary Search
- **Strictly Sorted Row-Major Matrix** (first element of row $r$ > last element of row $r-1$):
  - Flatten virtually into `[0 .. m*n - 1]` using `row = mid // n`, `col = mid % n`.
- **Row-and-Column Sorted Matrix** (each row and column sorted independently):
  - Start at top-right `(0, n - 1)`: if `val > target`, move left (`c -= 1`); if `val < target`, move down (`r += 1`). Runs in $O(m + n)$.

---

## Common Pitfalls & Edge Cases:
- **Infinite Loop on `left = mid`**:
  - Standard integer division `mid = (left + right) // 2` rounds **down** (`mid == left` when `right == left + 1`).
  - If your branch sets `left = mid` (for finding the *last* `True`), it will loop infinitely when `right - left == 1`!
  - **Fix**: Whenever using `left = mid`, bias midpoint **upward**: `mid = (left + right + 1) // 2`.
- **Comparing `nums[mid]` with `nums[left]` in Find Minimum**:
  - Comparing with `nums[left]` is ambiguous because `nums[left] < nums[mid]` holds both when the array is unrotated `[1, 2, 3, 4, 5]` (min on left) and when rotated `[3, 4, 5, 1, 2]` (min on right). Always compare `nums[mid]` with `nums[right]`.
- **Ceiling Division with Floats**:
  - Avoid `math.ceil(a / b)` on large integers due to float precision limits; use `(a + b - 1) // b`.
"""

from typing import Callable, List


# ============================================================================
# Template 1: Lower Bound (First index i where nums[i] >= target)
# ============================================================================
def template_lower_bound(nums: List[int], target: int) -> int:
    """
    Equivalent to bisect.bisect_left(nums, target).
    Returns len(nums) if all elements are < target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


# ============================================================================
# Template 2: Binary Search on Answer Space (Minimum Feasible Value)
# ============================================================================
def template_min_feasible_answer(low: int, high: int, is_feasible: Callable[[int], bool]) -> int:
    """
    Finds the minimum integer x in [low, high] such that is_feasible(x) is True.
    Assumes monotonicity: False, False, ..., False, True, True, ...
    Time: O(T_check * log(high - low)), Space: O(1)
    """
    left, right = low, high
    while left < right:
        mid = (left + right) // 2
        if is_feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left


# ============================================================================
# Template 3: Binary Search on Answer Space (Maximum Feasible Value)
# ============================================================================
def template_max_feasible_answer(low: int, high: int, is_feasible: Callable[[int], bool]) -> int:
    """
    Finds the maximum integer x in [low, high] such that is_feasible(x) is True.
    Assumes monotonicity: True, True, ..., True, False, False, ...
    Uses upper-midpoint to prevent infinite loops when setting left = mid.
    Time: O(T_check * log(high - low)), Space: O(1)
    """
    left, right = low, high
    while left < right:
        mid = (left + right + 1) // 2  # Upper mid required when assigning left = mid
        if is_feasible(mid):
            left = mid
        else:
            right = mid - 1
    return left

