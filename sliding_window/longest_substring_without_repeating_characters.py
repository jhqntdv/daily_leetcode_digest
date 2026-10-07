"""
Title: Longest Substring Without Repeating Characters
Difficulty: Medium
Tag: sliding_window

Problem Statement:
Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    print(f"Test 1: s = '{s1}' -> Output: {result1} (Expected: 3)")
    
    # Test Case 2
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"Test 2: s = '{s2}' -> Output: {result2} (Expected: 1)")
    
    # Test Case 3
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    print(f"Test 3: s = '{s3}' -> Output: {result3} (Expected: 3)")
