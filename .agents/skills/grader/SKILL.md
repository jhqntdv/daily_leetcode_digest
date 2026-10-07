---
name: grader
description: >-
  Use this skill when the user asks you to review, grade, stress test, or check their code implementation (especially for LeetCode or algorithmic challenges).
---

# Code Grader & Stress Tester

When the user asks you to grade, review, or stress test their code implementation, follow these steps to thoroughly evaluate their work.

## Steps

1. **Analyze the Implementation**: Carefully read the user's code. Identify the algorithm they are using, and determine both the time complexity and space complexity of their approach.
2. **Code Quality Review**:
   - Provide constructive feedback on code style, readability, and naming conventions.
   - Point out any immediate logical flaws, syntax issues, or anti-patterns.
3. **Generate Rigorous Test Cases (Stress Testing)**:
   - Formulate a comprehensive set of test cases, which must include:
     - **Standard cases**: Typical inputs the function is expected to handle.
     - **Edge cases**: Empty inputs, single-element inputs, negative numbers, all duplicates, etc.
     - **Stress cases**: Maximum possible constraints or large inputs to test performance boundaries.
4. **Execution & Validation**:
   - Mentally trace the user's code or write a quick test script using your execution tools to run the user's code against the generated test cases. Check if the outputs match the expected results.
5. **Performance Evaluation**:
   - Evaluate if the time and space complexity are optimal for the problem.
   - If there is a more efficient approach (e.g., $O(N \log N)$ instead of $O(N^2)$), explain the better approach or provide a gentle hint.
6. **Final Verdict & Feedback**:
   - Give the user a clear final verdict (e.g., "Pass ✅", "Needs Optimization ⚠️", or "Fails on Edge Cases ❌").
   - Summarize the actionable suggestions for improvement.
