"""
# Algorithm Cheat Sheet: Hash Tables (Maps & Sets)

## Core Patterns:
1. Complement Lookup (Two Sum Pattern):
   - Store seen elements and check if `target - num` exists.
   - O(n) time, O(n) space.

2. Canonical Form / Frequency Key (Group Anagrams Pattern):
   - Normalize string to a hashable tuple (sorted string or character frequency array).
   - Use as dict key to group elements: `defaultdict(list)`.

3. Counting & Frequency Tracking:
   - `collections.Counter`: frequency count, majority element, anagrams.

4. Set for O(1) Membership & Deduplication:
   - Longest Consecutive Sequence: only start search when `num - 1 not in s`.
"""

from collections import defaultdict, Counter

def template_two_sum(nums: list[int], target: int) -> list[int]:
    """Pattern: Check complement in map."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def template_group_canonical(items: list[str]) -> list[list[str]]:
    """Pattern: Group by frequency key."""
    groups = defaultdict(list)
    for s in items:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())
