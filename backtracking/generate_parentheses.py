"""
Problem: Generate Parentheses
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Example 3:
    Input: n = 2
    Output: ["(())","()()"]

Constraints:
    - 1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 3
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result1 = solution.generateParenthesis(n1)
    print(f"Test Case 1: n = {n1}")
    print(f"Result: {result1}")
    print(f"Matches Expected (order-independent): {sorted(result1 or []) == sorted(expected1)}\n")

    # Test Case 2
    n2 = 1
    expected2 = ["()"]
    result2 = solution.generateParenthesis(n2)
    print(f"Test Case 2: n = {n2}")
    print(f"Result: {result2}")
    print(f"Matches Expected (order-independent): {sorted(result2 or []) == sorted(expected2)}\n")

    # Test Case 3
    n3 = 2
    expected3 = ["(())", "()()"]
    result3 = solution.generateParenthesis(n3)
    print(f"Test Case 3: n = {n3}")
    print(f"Result: {result3}")
    print(f"Matches Expected (order-independent): {sorted(result3 or []) == sorted(expected3)}\n")
