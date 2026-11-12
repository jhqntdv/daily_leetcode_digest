"""
Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0, 1, 1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Example 3:
Input: n = 0
Output: [0]

Constraints:
- 0 <= n <= 10^5
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 2
    print(f"Test 1 - Input: n = {n1}")
    print(f"Output: {solution.countBits(n1)}")
    print(f"Expected: [0, 1, 1]\n")

    # Test Case 2
    n2 = 5
    print(f"Test 2 - Input: n = {n2}")
    print(f"Output: {solution.countBits(n2)}")
    print(f"Expected: [0, 1, 1, 2, 1, 2]\n")

    # Test Case 3
    n3 = 0
    print(f"Test 3 - Input: n = {n3}")
    print(f"Output: {solution.countBits(n3)}")
    print(f"Expected: [0]\n")
