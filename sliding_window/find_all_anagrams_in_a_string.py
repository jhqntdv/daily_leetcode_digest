class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Given two strings s and p, return an array of all the start indices of p's anagrams in s.
        You may return the answer in any order.

        Example 1:
        Input: s = "cbaebabacd", p = "abc"
        Output: [0,6]
        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".

        Example 2:
        Input: s = "abab", p = "ab"
        Output: [0,1,2]
        Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".

        Example 3:
        Input: s = "af", p = "be"
        Output: []

        Constraints:
        - 1 <= s.length, p.length <= 3 * 10^4
        - s and p consist of lowercase English letters.
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1, p1 = "cbaebabacd", "abc"
    print(f"Test 1: s = '{s1}', p = '{p1}'")
    print(f"Output: {sol.findAnagrams(s1, p1)} | Expected: [0, 6]\n")

    # Test Case 2
    s2, p2 = "abab", "ab"
    print(f"Test 2: s = '{s2}', p = '{p2}'")
    print(f"Output: {sol.findAnagrams(s2, p2)} | Expected: [0, 1, 2]\n")

    # Test Case 3
    s3, p3 = "af", "be"
    print(f"Test 3: s = '{s3}', p = '{p3}'")
    print(f"Output: {sol.findAnagrams(s3, p3)} | Expected: []")
