```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Given a string `s`, return `true` if the `s` can be a palindrome
        after deleting at most one character from it.

        Examples:
        1. s = "aba" -> true
        2. s = "abca" -> true (delete 'c')
        3. s = "abc" -> false

        Constraints:
        * 1 <= s.length <= 10^5
        * s consists of lowercase English letters.
        """
        # Your code here
        pass

if __name__ == '__main__':
    sol = Solution()
    
    # Example 1
    s1 = "aba"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {sol.validPalindrome(s1)}") # Expected: True

    # Example 2
    s2 = "abca"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {sol.validPalindrome(s2)}") # Expected: True

    # Example 3
    s3 = "abc"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {sol.validPalindrome(s3)}") # Expected: False

    # Additional Test Case
    s4 = "cbbcc"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {sol.validPalindrome(s4)}") # Expected: True (delete one 'c' or 'b')

    s5 = "eeccccbebaeeabebccceea"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {sol.validPalindrome(s5)}") # Expected: False

    s6 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(f"Input: s = \"{s6}\"")
    print(f"Output: {sol.validPalindrome(s6)}") # Expected: True
```