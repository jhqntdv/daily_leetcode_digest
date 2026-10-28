class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest
        common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string
        with some characters (can be none) deleted without changing the relative order
        of the remaining characters.
        (e.g., "ace" is a subsequence of "abcde" while "aec" is not).
        A common subsequence of two strings is a subsequence that is common to both strings.

        Difficulty: Medium
        Tag: dynamic_programming

        Constraints:
            - 1 <= len(text1), len(text2) <= 1000
            - text1 and text2 consist of only lowercase English characters.
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    text1_1, text2_1 = "abcde", "ace"
    print(f"Test 1: text1='{text1_1}', text2='{text2_1}'")
    print(f"Output: {sol.longestCommonSubsequence(text1_1, text2_1)} | Expected: 3\n")

    # Test Case 2
    text1_2, text2_2 = "abc", "abc"
    print(f"Test 2: text1='{text1_2}', text2='{text2_2}'")
    print(f"Output: {sol.longestCommonSubsequence(text1_2, text2_2)} | Expected: 3\n")

    # Test Case 3
    text1_3, text2_3 = "abc", "def"
    print(f"Test 3: text1='{text1_3}', text2='{text2_3}'")
    print(f"Output: {sol.longestCommonSubsequence(text1_3, text2_3)} | Expected: 0\n")
