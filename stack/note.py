"""
# Algorithm Cheat Sheet: Stack

## Core Patterns:
1. Matching Pairs (LIFO):
   - Push opening elements, pop and validate on closing elements.
   - Example: Valid Parentheses, HTML/XML tag validator.

2. Monotonic Stack:
   - Maintains elements in strictly increasing or decreasing order.
   - Use for: Next Greater Element, Daily Temperatures, Largest Rectangle in Histogram.
   - Template:
     ```python
     stack = []
     for i, x in enumerate(nums):
         while stack and nums[stack[-1]] < x:
             prev_idx = stack.pop()
             res[prev_idx] = x
         stack.append(i)
     ```

3. Expression Evaluation / Parsing:
   - Polish notation, basic calculator, decoding strings (e.g., `3[a2[c]]`).
"""

def template_valid_parentheses(s: str) -> bool:
    """Validate balanced parentheses using a stack."""
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

def template_next_greater_element(nums: list[int]) -> list[int]:
    """Monotonic decreasing stack for next greater element."""
    res = [-1] * len(nums)
    stack = []  # stores indices
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        stack.append(i)
    return res
