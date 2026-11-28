"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Difficulty: Medium

Examples:
    Example 1:
        Input: x = 2.00000, n = 10
        Output: 1024.00000

    Example 2:
        Input: x = 2.10000, n = 3
        Output: 9.26100

    Example 3:
        Input: x = 2.00000, n = -2
        Output: 0.25000
        Explanation: 2^-2 = 1/(2^2) = 1/4 = 0.25

Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31 - 1
    - n is an integer.
    - Either x != 0 or n > 0.
    - -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    x1, n1 = 2.00000, 10
    result1 = solution.myPow(x1, n1)
    print(f"Test 1: x = {x1}, n = {n1} -> Output: {result1:.5f} (Expected: 1024.00000)")

    # Test Case 2
    x2, n2 = 2.10000, 3
    result2 = solution.myPow(x2, n2)
    print(f"Test 2: x = {x2}, n = {n2} -> Output: {result2:.5f} (Expected: 9.26100)")

    # Test Case 3
    x3, n3 = 2.00000, -2
    result3 = solution.myPow(x3, n3)
    print(f"Test 3: x = {x3}, n = {n3} -> Output: {result3:.5f} (Expected: 0.25000)")
