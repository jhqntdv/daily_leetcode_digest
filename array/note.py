"""
# Algorithm Cheat Sheet: Arrays & In-Place Indexing

## Core Patterns:
1. **Index as Hash Key (In-Place Marking)**:
   - When `nums` are in range `[1, n]` or `[0, n-1]` with size `n`.
   - Use sign negation: `nums[abs(x) - 1] *= -1` to mark visited in $O(1)$ extra space.
   - Use cyclic sort / swaps: place `nums[i]` at `nums[nums[i] - 1]`.
   - Time: $O(n)$, Space: $O(1)$.

2. **Prefix & Suffix Decomposition**:
   - **Prefix Sum**: `sum(nums[i..j]) = prefix[j+1] - prefix[i]`.
   - **Subarray Sum Equals K**: Hash map tracking frequencies of running prefix sums (`curr_sum - k`).
   - **Prefix & Suffix Product (`Product Except Self`)**:
     - Pass 1 (Left-to-Right): Write running `prefix` product into `ans[i]`.
     - Pass 2 (Right-to-Left): Multiply running `suffix` product into `ans[i]`.
     - Avoids division by zero and uses $O(1)$ extra space beyond the output array.

3. **Single-Pass Running Extremum & Kadane's Algorithm**:
   - **Running Minimum / Maximum Difference (`Best Time to Buy and Sell Stock`)**:
     - Track `min_so_far` and maximize `price - min_so_far` at each step.
   - **Kadane's Algorithm (`Maximum Subarray`)**:
     - `curr_max = max(num, curr_max + num)`
     - `global_max = max(global_max, curr_max)`

---

## Common Pitfalls & Edge Cases:
- **Zero Elements in Product Problems**: Never divide the total product by `nums[i]` without handling `0` (single zero vs. multiple zeros). Use prefix/suffix multiplication instead.
- **Mutating Input Array**: In-place sign marking mutates `nums`. If callers require the original array intact, restore signs with `nums[i] = abs(nums[i])` in a cleanup pass.
"""


def template_index_hash(nums: list[int]) -> list[int]:
    """Pattern: Find duplicates in [1, n] range in O(n) time and O(1) space."""
    res = []
    for x in nums:
        idx = abs(x) - 1
        if nums[idx] < 0:
            res.append(abs(x))
        else:
            nums[idx] = -nums[idx]
    return res


def template_prefix_sum(nums: list[int], k: int) -> int:
    """Pattern: Number of subarrays summing to k in O(n) time."""
    count, curr_sum = 0, 0
    prefix_counts = {0: 1}
    for x in nums:
        curr_sum += x
        count += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
    return count


def template_prefix_suffix_product(nums: list[int]) -> list[int]:
    """Pattern: Product of array except self in O(n) time and O(1) extra space."""
    n = len(nums)
    ans = [1] * n
    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]
    return ans


def template_running_min_max_diff(prices: list[int]) -> int:
    """Pattern: Maximum difference prices[j] - prices[i] for j > i in O(n) time."""
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
