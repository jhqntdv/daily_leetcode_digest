"""
# Algorithm Cheat Sheet: Arrays & In-Place Indexing

## Core Patterns:
1. Index as Hash Key:
   - When nums are in range [1, n] or [0, n-1] with size n.
   - Use sign negation: `nums[abs(x) - 1] *= -1` to mark visited.
   - Use cyclic sort / swaps: place `nums[i]` at `nums[nums[i] - 1]`.
   - Time: O(n), Space: O(1).

2. Prefix Sum:
   - Range sum queries: `sum(nums[i..j]) = prefix[j+1] - prefix[i]`.
   - Subarray sum equals k: Hash map tracking frequencies of running prefix sums.

3. Kadane's Algorithm (Max Subarray):
   - `curr_max = max(num, curr_max + num)`
   - `global_max = max(global_max, curr_max)`
"""

def template_index_hash(nums: list[int]) -> list[int]:
    """Pattern: Find duplicates in [1, n] range in O(1) space."""
    res = []
    for x in nums:
        idx = abs(x) - 1
        if nums[idx] < 0:
            res.append(abs(x))
        else:
            nums[idx] = -nums[idx]
    return res

def template_prefix_sum(nums: list[int], k: int) -> int:
    """Pattern: Number of subarrays summing to k."""
    count, curr_sum = 0, 0
    prefix_counts = {0: 1}
    for x in nums:
        curr_sum += x
        count += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
    return count
