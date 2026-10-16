class Solution:
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Constraints:
            1 <= n <= 45

        Example 1:
            Input: n = 2
            Output: 2

        Example 2:
            Input: n = 3
            Output: 3

        Example 3:
            Input: n = 4
            Output: 5
        """
        # Write your solution here
        pass


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    n1 = 2
    print(f"Test 1: n = {n1} -> Output: {solution.climbStairs(n1)} (Expected: 2)")

    # Test Case 2
    n2 = 3
    print(f"Test 2: n = {n2} -> Output: {solution.climbStairs(n2)} (Expected: 3)")

    # Test Case 3
    n3 = 4
    print(f"Test 3: n = {n3} -> Output: {solution.climbStairs(n3)} (Expected: 5)")
