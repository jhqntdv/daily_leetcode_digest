class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.

        In other words, return True if one of s1's permutations is a substring of s2.

        Examples:
        Example 1:
            Input: s1 = "ab", s2 = "eidbaooo"
            Output: True
            Explanation: s2 contains one permutation of s1 ("ba").

        Example 2:
            Input: s1 = "ab", s2 = "eidboaoo"
            Output: False

        Example 3:
            Input: s1 = "adc", s2 = "dcda"
            Output: True
            Explanation: s2 contains permutation of s1 ("cda").

        Constraints:
        - 1 <= s1.length, s2.length <= 10^4
        - s1 and s2 consist of lowercase English letters.
        """
        # Write your code here
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1_1, s2_1 = "ab", "eidbaooo"
    print(f"Test 1: s1='{s1_1}', s2='{s2_1}' -> {sol.checkInclusion(s1_1, s2_1)} (Expected: True)")

    # Test case 2
    s1_2, s2_2 = "ab", "eidboaoo"
    print(f"Test 2: s1='{s1_2}', s2='{s2_2}' -> {sol.checkInclusion(s1_2, s2_2)} (Expected: False)")

    # Test case 3
    s1_3, s2_3 = "adc", "dcda"
    print(f"Test 3: s1='{s1_3}', s2='{s2_3}' -> {sol.checkInclusion(s1_3, s2_3)} (Expected: True)")
