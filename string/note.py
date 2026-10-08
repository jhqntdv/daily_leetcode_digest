"""
# Algorithm Cheat Sheet: Strings

## Core Patterns:
1. Two Pointers (Palindrome, Reversal):
   - Left and right pointers moving inward.

2. Sliding Window (Substrings):
   - Longest substring without repeating characters, Minimum Window Substring.

3. Character Counting & Frequency:
   - Fixed size array `[0] * 26` or `Counter(s)`.

4. Vertical Scanning / Trie:
   - Longest Common Prefix: scan character by character across all strings.
   - Prefix matching: Trie (Prefix Tree).
"""

def template_longest_common_prefix(strs: list[str]) -> str:
    """Vertical scanning: compare characters column by column."""
    if not strs:
        return ""
    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]

def template_is_palindrome(s: str) -> bool:
    """Two pointers checking alphanumeric palindrome."""
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
