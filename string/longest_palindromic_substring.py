class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.
        """
        # Your code here
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    s1 = "babad"
    # Expected: "bab" or "aba"
    result1 = sol.longestPalindrome(s1)
    print(f"Input: \"{s1}\", Output: \"{result1}\"")
    assert result1 == "bab" or result1 == "aba", f"Test Case 1 Failed: Expected 'bab' or 'aba', Got '{result1}'"

    # Test Case 2
    s2 = "cbbd"
    # Expected: "bb"
    result2 = sol.longestPalindrome(s2)
    print(f"Input: \"{s2}\", Output: \"{result2}\"")
    assert result2 == "bb", f"Test Case 2 Failed: Expected 'bb', Got '{result2}'"

    # Test Case 3
    s3 = "a"
    # Expected: "a"
    result3 = sol.longestPalindrome(s3)
    print(f"Input: \"{s3}\", Output: \"{result3}\"")
    assert result3 == "a", f"Test Case 3 Failed: Expected 'a', Got '{result3}'"

    print("\nAll test cases passed!")
