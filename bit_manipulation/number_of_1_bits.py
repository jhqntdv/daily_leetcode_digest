class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Given a positive integer n, return the number of set bits (1s) it has
        (also known as the Hamming weight).

        Constraints:
        - 1 <= n <= 2^31 - 1
        """
        # Write your solution here
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 11  # Binary: 00000000000000000000000000001011
    print(f"Test 1: n = {n1} -> Output: {solution.hammingWeight(n1)} (Expected: 3)")

    # Test Case 2
    n2 = 128  # Binary: 00000000000000000000000010000000
    print(f"Test 2: n = {n2} -> Output: {solution.hammingWeight(n2)} (Expected: 1)")

    # Test Case 3
    n3 = 2147483645  # Binary: 01111111111111111111111111111101
    print(f"Test 3: n = {n3} -> Output: {solution.hammingWeight(n3)} (Expected: 30)")
