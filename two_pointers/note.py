"""
# Algorithm Cheat Sheet: Two Pointers

## Core Patterns:
1. Inward-Moving Pointers (Opposite Ends):
   - Sorted array (Two Sum II, 3Sum, 4Sum).
   - Greedy shrink (Container With Most Water: move pointer with smaller height).
   - Palindrome checks and string reversals.

2. Fast and Slow Pointers (Floyd's Cycle Detection / Tortoise & Hare):
   - Finding cycle in linked list or array mapped to index pointers (Find the Duplicate Number).
   - Phase 1: `slow = f(slow)`, `fast = f(f(fast))` until `slow == fast`.
   - Phase 2: `slow = start`, move both by 1 step until they meet at cycle entrance.

3. Forward-Moving / Read-Write Pointers:
   - Remove duplicates in-place (`nums[slow] = nums[fast]`).
   - Move zeroes.
"""

def template_opposite_ends(nums: list[int], target: int) -> list[int]:
    """Two Sum II in sorted array."""
    l, r = 0, len(nums) - 1
    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return [l, r]
        elif curr < target:
            l += 1
        else:
            r -= 1
    return []

def template_floyd_cycle(nums: list[int]) -> int:
    """Find duplicate number via Floyd's cycle detection."""
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
