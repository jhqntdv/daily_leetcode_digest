"""
# Algorithm Cheat Sheet: Sliding Window

## Core Patterns:
1. Dynamic Window (Find Longest / Shortest Subarray/Substring):
   - Expand right pointer `r`.
   - When condition violated, shrink left pointer `l`.
   - Update answer either on valid condition (longest) or inside while loop (shortest).

2. Fixed-Size Window:
   - Window size `k` is fixed.
   - Slide window: add `nums[i]`, remove `nums[i - k]`.

3. Hash Map / Frequency Counter with Window:
   - Track characters in window: `Counter` or `last_seen` dictionary.
   - Jump `l` directly: `l = max(l, last_seen[char] + 1)`.
"""

def template_longest_window(s: str) -> int:
    """Pattern: Longest substring without repeating characters."""
    last_seen = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def template_fixed_window(nums: list[int], k: int) -> int:
    """Pattern: Maximum sum of subarray of fixed size k."""
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum
