"""
Valid Anagram

Difficulty: Easy

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

Example 3:
Input: s = "listen", t = "silent"
Output: True

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

def isAnagram(s: str, t: str) -> bool:
    # Write your solution here
    pass


if __name__ == '__main__':
    # Test Case 1
    s1, t1 = "anagram", "nagaram"
    print(f"Test 1: s = '{s1}', t = '{t1}' -> Expected: True | Got: {isAnagram(s1, t1)}")

    # Test Case 2
    s2, t2 = "rat", "car"
    print(f"Test 2: s = '{s2}', t = '{t2}' -> Expected: False | Got: {isAnagram(s2, t2)}")

    # Test Case 3
    s3, t3 = "listen", "silent"
    print(f"Test 3: s = '{s3}', t = '{t3}' -> Expected: True | Got: {isAnagram(s3, t3)}")
