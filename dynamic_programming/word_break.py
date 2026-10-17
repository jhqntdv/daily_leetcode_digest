"""
Word Break (LeetCode #139)
Difficulty: Medium

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in
the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: True
    Explanation: Return True because "leetcode" can be segmented as "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: True
    Explanation: Return True because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.

Example 3:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: False

Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters.
    - All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(f"Test 1: {solution.wordBreak(s1, wordDict1)} (Expected: True)")

    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(f"Test 2: {solution.wordBreak(s2, wordDict2)} (Expected: True)")

    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"Test 3: {solution.wordBreak(s3, wordDict3)} (Expected: False)")
