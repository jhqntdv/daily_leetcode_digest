class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Title: Reverse Bits
        Difficulty: Easy

        Problem Statement:
        Reverse bits of a given 32-bit unsigned integer.

        Examples:
        Example 1:
        Input: n = 43261596 (binary: 00000010100101000001111010011100)
        Output: 964176192 (binary: 00111001011110000010100101000000)
        Explanation: The input binary string 00000010100101000001111010011100 represents
        the unsigned integer 43261596, so return 964176192 which has binary representation
        00111001011110000010100101000000.

        Example 2:
        Input: n = 4294967293 (binary: 11111111111111111111111111111101)
        Output: 3221225471 (binary: 10111111111111111111111111111111)

        Example 3:
        Input: n = 0
        Output: 0

        Constraints:
        - The input must be a 32-bit unsigned integer.
        """
        pass


if __name__ == '__main__':
    sol = Solution()

    # Test Case 1
    n1 = 43261596
    print(f"Test 1: Input = {n1}, Output = {sol.reverseBits(n1)} (Expected: 964176192)")

    # Test Case 2
    n2 = 4294967293
    print(f"Test 2: Input = {n2}, Output = {sol.reverseBits(n2)} (Expected: 3221225471)")

    # Test Case 3
    n3 = 0
    print(f"Test 3: Input = {n3}, Output = {sol.reverseBits(n3)} (Expected: 0)")
