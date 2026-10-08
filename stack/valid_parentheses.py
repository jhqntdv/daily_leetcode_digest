"""
Title: Valid Parentheses (LeetCode 20)
Difficulty: Easy
Tag: stack

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: True

Example 2:
    Input: s = "()[]{}"
    Output: True

Example 3:
    Input: s = "(]"
    Output: False

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "()"
    expected1 = True
    result1 = solution.isValid(s1)
    print(f"Test Case 1: s = '{s1}' -> Result: {result1} | Expected: {expected1} | {'PASS' if result1 == expected1 else 'FAIL'}")

    # Test Case 2
    s2 = "()[]{}"
    expected2 = True
    result2 = solution.isValid(s2)
    print(f"Test Case 2: s = '{s2}' -> Result: {result2} | Expected: {expected2} | {'PASS' if result2 == expected2 else 'FAIL'}")

    # Test Case 3
    s3 = "(]"
    expected3 = False
    result3 = solution.isValid(s3)
    print(f"Test Case 3: s = '{s3}' -> Result: {result3} | Expected: {expected3} | {'PASS' if result3 == expected3 else 'FAIL'}")
