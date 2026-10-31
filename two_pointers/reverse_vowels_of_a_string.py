class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and return it.
        The vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper cases.

        Example 1:
        Input: s = "hello"
        Output: "holle"

        Example 2:
        Input: s = "leetcode"
        Output: "leotcede"

        Example 3:
        Input: s = "aA"
        Output: "Aa"

        Constraints:
        1 <= s.length <= 3 * 10^5
        s consists of printable ASCII characters.
        """
        # Your code here
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test cases
    test_cases = [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
        ("", ""),
        ("bcdfgh", "bcdfgh"),
        ("AEIOU", "UOIEA"),
        ("Design", "Desing")
    ]

    for input_str, expected_output in test_cases:
        actual_output = sol.reverseVowels(input_str)
        print(f"Input: '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'")
        assert actual_output == expected_output, f"Test failed for input '{input_str}'. Expected '{expected_output}', got '{actual_output}'"
        print(f"Test passed for input '{input_str}'")

    print("All test cases passed!")
