"""
Title: Group Anagrams
Difficulty: Medium
Tag: hash_table

Problem Statement:
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    test1 = ["eat","tea","tan","ate","nat","bat"]
    print("Test 1 Output:", solution.groupAnagrams(test1))

    # Test Case 2
    test2 = [""]
    print("Test 2 Output:", solution.groupAnagrams(test2))

    # Test Case 3
    test3 = ["a"]
    print("Test 3 Output:", solution.groupAnagrams(test3))
