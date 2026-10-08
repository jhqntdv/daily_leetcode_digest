class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a 
        different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Constraints:
        - 1 <= prices.length <= 10^5
        - 0 <= prices[i] <= 10^4
        """
        # Write your code here
        return 0

if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test Case 1: Input: {prices1} | Expected: 5 | Got: {sol.maxProfit(prices1)}")
    
    # Test Case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test Case 2: Input: {prices2} | Expected: 0 | Got: {sol.maxProfit(prices2)}")
    
    # Test Case 3
    prices3 = [2, 4, 1]
    print(f"Test Case 3: Input: {prices3} | Expected: 2 | Got: {sol.maxProfit(prices3)}")
