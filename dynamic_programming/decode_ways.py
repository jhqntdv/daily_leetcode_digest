class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Given a string s containing digits, return the number of ways to decode it.

        A message containing letters from A-Z can be encoded into numbers using:
        'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

        :type s: str
        :rtype: int
        """
        # TODO: Implement your solution here
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    s1 = "12"
    print(f"Test 1: s = '{s1}' -> Result: {sol.numDecodings(s1)} (Expected: 2)")

    # Test Case 2
    s2 = "226"
    print(f"Test 2: s = '{s2}' -> Result: {sol.numDecodings(s2)} (Expected: 3)")

    # Test Case 3
    s3 = "06"
    print(f"Test 3: s = '{s3}' -> Result: {sol.numDecodings(s3)} (Expected: 0)")
