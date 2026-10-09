"""
Title: Coin Change
Difficulty: Medium
Tag: dynamic_programming

Problem Statement:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    coins1, amount1 = [1, 2, 5], 11
    print(f"Test 1: coins={coins1}, amount={amount1} -> Result: {sol.coinChange(coins1, amount1)} (Expected: 3)")

    # Test Case 2
    coins2, amount2 = [2], 3
    print(f"Test 2: coins={coins2}, amount={amount2} -> Result: {sol.coinChange(coins2, amount2)} (Expected: -1)")

    # Test Case 3
    coins3, amount3 = [1], 0
    print(f"Test 3: coins={coins3}, amount={amount3} -> Result: {sol.coinChange(coins3, amount3)} (Expected: 0)")
