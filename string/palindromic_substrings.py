class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Given a string s, return the number of palindromic substrings in it.

        A substring is a contiguous sequence of characters within the string.

        Example 1:
        Input: s = "abc"
        Output: 3
        Explanation: Three palindromic substrings: "a", "b", "c".

        Example 2:
        Input: s = "aaa"
        Output: 6
        Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".

        Example 3:
        Input: s = "aba"
        Output: 4
        Explanation: Four palindromic substrings: "a", "b", "a", "aba".

        Constraints:
        1 <= s.length <= 1000
        s consists of lowercase English letters.
        """
        pass

if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    s1 = "abc"
    expected1 = 3
    result1 = sol.countSubstrings(s1)
    print(f"Input: {s1}, Output: {result1}, Expected: {expected1} -> {'Passed' if result1 == expected1 else 'Failed'}")

    # Test Case 2
    s2 = "aaa"
    expected2 = 6
    result2 = sol.countSubstrings(s2)
    print(f"Input: {s2}, Output: {result2}, Expected: {expected2} -> {'Passed' if result2 == expected2 else 'Failed'}")

    # Test Case 3
    s3 = "aba"
    expected3 = 4
    result3 = sol.countSubstrings(s3)
    print(f"Input: {s3}, Output: {result3}, Expected: {expected3} -> {'Passed' if result3 == expected3 else 'Failed'}")

    # Additional Test Case
    s4 = "aab"
    expected4 = 4 # "a", "a", "b", "aa"
    result4 = sol.countSubstrings(s4)
    print(f"Input: {s4}, Output: {result4}, Expected: {expected4} -> {'Passed' if result4 == expected4 else 'Failed'}")
