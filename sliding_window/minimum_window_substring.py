class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum window 
        substring of s such that every character in t (including duplicates) is included in the window. 
        If there is no such substring, return the empty string "".

        Example 1:
            Input: s = "ADOBECODEBANC", t = "ABC"
            Output: "BANC"
            Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        Example 2:
            Input: s = "a", t = "a"
            Output: "a"
            Explanation: The entire string s is the minimum window.

        Example 3:
            Input: s = "a", t = "aa"
            Output: ""
            Explanation: Both 'a's from t must be included in the window.
            Since the largest window of s only has one 'a', return empty string.

        Constraints:
            - m == s.length
            - n == t.length
            - 1 <= m, n <= 10^5
            - s and t consist of uppercase and lowercase English letters.
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1, t1 = "ADOBECODEBANC", "ABC"
    print(f"Test 1: s = '{s1}', t = '{t1}'")
    print(f"Output: '{sol.minWindow(s1, t1)}'")
    print(f"Expected: 'BANC'\n")

    # Test Case 2
    s2, t2 = "a", "a"
    print(f"Test 2: s = '{s2}', t = '{t2}'")
    print(f"Output: '{sol.minWindow(s2, t2)}'")
    print(f"Expected: 'a'\n")

    # Test Case 3
    s3, t3 = "a", "aa"
    print(f"Test 3: s = '{s3}', t = '{t3}'")
    print(f"Output: '{sol.minWindow(s3, t3)}'")
    print(f"Expected: ''\n")
