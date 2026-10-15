"""
Title: Longest Repeating Character Replacement
Difficulty: Medium

Problem Statement:
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation
at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exist other ways to achieve this answer too.

Example 3:
Input: s = "AAAA", k = 2
Output: 4
Explanation: No replacements needed, all characters are already identical.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1, k1 = "ABAB", 2
    print(f"Test 1: s = '{s1}', k = {k1}")
    print(f"Output: {solution.characterReplacement(s1, k1)} | Expected: 4\n")

    # Test case 2
    s2, k2 = "AABABBA", 1
    print(f"Test 2: s = '{s2}', k = {k2}")
    print(f"Output: {solution.characterReplacement(s2, k2)} | Expected: 4\n")

    # Test case 3
    s3, k3 = "AAAA", 2
    print(f"Test 3: s = '{s3}', k = {k3}")
    print(f"Output: {solution.characterReplacement(s3, k3)} | Expected: 4\n")
