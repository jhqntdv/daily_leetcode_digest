---
name: daily-leetcode
description: >-
  Use this skill when the user asks for their daily digest, daily LeetCode, or a coding challenge.
---

# Daily LeetCode Digest

When the user asks for their daily LeetCode or daily digest, follow these instructions to present them with a challenge.

## Steps

1. Select a random **Easy** or **Medium** difficulty algorithm problem (similar to classic LeetCode questions).
2. Determine the primary **Tag** for this question (e.g., `two_pointers`, `greedy`, `math`, `dynamic_programming`, `hash_table`).
3. Present the problem to the user in a clean, readable markdown format. Include:
   - **Title & Difficulty**
   - **Problem Statement**, exactly 3 **Examples** (test cases), and **Constraints**.
4. **Create the workspace files automatically**:
   - Create a folder named after the question's tag in the root of the project (e.g., `two_pointers/`).
   - Inside that folder, create a Python file named after the problem (e.g., `two_pointers/two_sum.py`).
   - Write the starter code into this file. Include a docstring with the problem description and a simple `if __name__ == '__main__':` block that sets up 3 example test cases so the user can run them immediately.
5. **Crucial Rule**: DO NOT provide the solution logic or any major hints unless the user explicitly asks for them. Your goal is to let them practice and write the code themselves. 
6. End your response by encouraging them to open the newly created file and start coding their solution!
