from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Title: Asteroid Collision
        Difficulty: Medium
        LeetCode: 735

        Problem Statement:
        We are given an array asteroids of integers representing asteroids in a row.
        For each asteroid, the absolute value represents its size, and the sign represents
        its direction (positive meaning right, negative meaning left). Each asteroid moves
        at the same speed.

        Find out the state of the asteroids after all collisions. If two asteroids meet,
        the smaller one will explode. If both are the same size, both will explode. Two
        asteroids moving in the same direction will never meet.

        Example 1:
        Input: asteroids = [5, 10, -5]
        Output: [5, 10]
        Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

        Example 2:
        Input: asteroids = [8, -8]
        Output: []
        Explanation: The 8 and -8 collide exploding each other.

        Example 3:
        Input: asteroids = [10, 2, -5]
        Output: [10]
        Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

        Constraints:
        - 2 <= asteroids.length <= 10^4
        - -1000 <= asteroids[i] <= 1000
        - asteroids[i] != 0
        """
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    asteroids1 = [5, 10, -5]
    expected1 = [5, 10]
    result1 = solution.asteroidCollision(asteroids1)
    print(f"Test 1: asteroids = {asteroids1}")
    print(f"Output: {result1} | Expected: {expected1} | {'PASS' if result1 == expected1 else 'FAIL'}\n")

    # Test Case 2
    asteroids2 = [8, -8]
    expected2 = []
    result2 = solution.asteroidCollision(asteroids2)
    print(f"Test 2: asteroids = {asteroids2}")
    print(f"Output: {result2} | Expected: {expected2} | {'PASS' if result2 == expected2 else 'FAIL'}\n")

    # Test Case 3
    asteroids3 = [10, 2, -5]
    expected3 = [10]
    result3 = solution.asteroidCollision(asteroids3)
    print(f"Test 3: asteroids = {asteroids3}")
    print(f"Output: {result3} | Expected: {expected3} | {'PASS' if result3 == expected3 else 'FAIL'}\n")
