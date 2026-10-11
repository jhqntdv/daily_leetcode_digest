"""
# Algorithm Cheat Sheet: Greedy Algorithms

## Core Concepts & Guarantees:
A greedy algorithm makes the locally optimal choice at each stage with the hope of finding a global optimum.
It works when a problem exhibits:
1. **Greedy-Choice Property**: A global optimum can be reached by selecting local optima without reconsidering earlier choices.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to subproblems.

---

## Core Patterns:

1. **Horizon / Reachability Expansion (Jump Game & Variants)**:
   - Track `max_reach` or the current coverage window `[cur_end, next_max]`.
   - Iterate through indices; if `i > max_reach`, the boundary cannot be bridged.
   - Advance greedy step count when `i == cur_end`.

2. **Interval Scheduling / Selection**:
   - Sort intervals by **end time** (`key=lambda x: x[1]`).
   - Greedily pick the interval that finishes earliest to leave maximum room for remaining intervals.

3. **Running Balance & Reset (Gas Station / Kadane's-style)**:
   - If accumulated profit/gas dips below zero, any starting point within that prefix is invalid.
   - Greedily reset starting point to `i + 1` and reset the current accumulator.

4. **Two-Pass Greedy (Bidirectional Constraints - e.g., Candy)**:
   - Pass 1 (Left-to-Right): satisfy relation `nums[i] > nums[i-1]`.
   - Pass 2 (Right-to-Left): satisfy relation `nums[i] > nums[i+1]` using `max(res[i], res[i+1] + 1)`.

---

## Common Pitfalls & Edge Cases:
- **False Greedy**: Not all optimization problems can be solved greedily (e.g., 0/1 Knapsack, Coin Change with arbitrary denominations require Dynamic Programming). Always test counterexamples.
- **Sorting Metric**: Sorting by start time vs. end time. Interval scheduling (max intervals) requires sorting by end time, whereas interval merging requires sorting by start time.
- **Zeros and Single-Element Inputs**: Check inputs like `[0]`, `[0, 1]`, or empty collections.
"""

from typing import List


def template_reachability_min_steps(nums: List[int]) -> int:
    """
    Pattern: Minimum jumps/steps to reach the end (Jump Game II).
    Greedily expands coverage horizon [cur_end, next_end].
    Time: O(n), Space: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    cur_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
            if cur_end >= len(nums) - 1:
                break

    return jumps


def template_interval_scheduling(intervals: List[List[int]]) -> int:
    """
    Pattern: Maximum number of mutually compatible intervals.
    Sort by end time; pick interval with earliest end time.
    Time: O(n log n), Space: O(1) or O(n) depending on sort implementation
    """
    if not intervals:
        return 0

    # Sort primarily by end time
    intervals.sort(key=lambda x: x[1])

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count


def template_two_pass_bidirectional(ratings: List[int]) -> int:
    """
    Pattern: Two-pass greedy for bidirectional neighbor constraints (e.g., Candy).
    Time: O(n), Space: O(n)
    """
    n = len(ratings)
    alloc = [1] * n

    # Pass 1: Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            alloc[i] = alloc[i - 1] + 1

    # Pass 2: Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            alloc[i] = max(alloc[i], alloc[i + 1] + 1)

    return sum(alloc)
