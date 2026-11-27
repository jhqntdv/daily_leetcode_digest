"""
Coin Change II

You are given an integer array `coins` representing coins of different denominations 
and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: There are four ways to make up the amount:
5 = 5
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    amount1 = 5
    coins1 = [1, 2, 5]
    print(f"Example 1: amount = {amount1}, coins = {coins1}")
    print(f"Output: {sol.change(amount1, coins1)}")  # Expected: 4
    print("-" * 40)

    # Example 2
    amount2 = 3
    coins2 = [2]
    print(f"Example 2: amount = {amount2}, coins = {coins2}")
    print(f"Output: {sol.change(amount2, coins2)}")  # Expected: 0
    print("-" * 40)

    # Example 3
    amount3 = 10
    coins3 = [10]
    print(f"Example 3: amount = {amount3}, coins = {coins3}")
    print(f"Output: {sol.change(amount3, coins3)}")  # Expected: 1
    print("-" * 40)
