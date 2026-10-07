from typing import List

class Solution:
    """
    Title: Container With Most Water
    Difficulty: Medium

    Problem Statement:
    You are given an integer array height of length n. There are n vertical lines drawn 
    such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container 
    contains the most water.

    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Examples:
    Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
                     In this case, the max area of water the container can contain is 49.

    Example 2:
        Input: height = [1,1]
        Output: 1

    Example 3:
        Input: height = [4,3,2,1,4]
        Output: 16

    Constraints:
        - n == height.length
        - 2 <= n <= 10^5
        - 0 <= height[i] <= 10^4
    """
    def maxArea(self, height: List[int]) -> int:
        # Write your code here
        pass

if __name__ == '__main__':
    solution = Solution()
    
    # Test Case 1
    tc1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    result1 = solution.maxArea(tc1)
    print(f"Test Case 1: {'PASSED' if result1 == expected1 else 'FAILED'} (Expected: {expected1}, Got: {result1})")

    # Test Case 2
    tc2 = [1,1]
    expected2 = 1
    result2 = solution.maxArea(tc2)
    print(f"Test Case 2: {'PASSED' if result2 == expected2 else 'FAILED'} (Expected: {expected2}, Got: {result2})")

    # Test Case 3
    tc3 = [4,3,2,1,4]
    expected3 = 16
    result3 = solution.maxArea(tc3)
    print(f"Test Case 3: {'PASSED' if result3 == expected3 else 'FAILED'} (Expected: {expected3}, Got: {result3})")
