class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.

        A word is defined as a sequence of non-space characters. The words in s
        will be separated by at least one space.

        Return a string of the words in reverse order concatenated by a single space.

        Note that s may contain leading or trailing spaces or multiple spaces between two words.
        The returned string should only have a single space separating the words.
        Do not include any extra spaces.

        Example 1:
            Input: s = "the sky is blue"
            Output: "blue is sky the"

        Example 2:
            Input: s = "  hello world  "
            Output: "world hello"

        Example 3:
            Input: s = "a good   example"
            Output: "example good a"

        Constraints:
            - 1 <= s.length <= 10^4
            - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
            - There is at least one word in s.
        """
        pass


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "the sky is blue"
    print(f"Test Case 1: s = '{s1}'")
    print(f"Output: '{solution.reverseWords(s1)}'\n")

    # Example 2
    s2 = "  hello world  "
    print(f"Test Case 2: s = '{s2}'")
    print(f"Output: '{solution.reverseWords(s2)}'\n")

    # Example 3
    s3 = "a good   example"
    print(f"Test Case 3: s = '{s3}'")
    print(f"Output: '{solution.reverseWords(s3)}'\n")
