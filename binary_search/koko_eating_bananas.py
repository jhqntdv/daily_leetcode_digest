import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are n piles of bananas, the i-th pile has piles[i] bananas.
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile
        of bananas and eats k bananas from that pile. If the pile has less than k bananas, she
        eats all of them instead and will not eat any more bananas during this hour.

        Return the minimum integer k such that she can eat all the bananas within h hours.

        Constraints:
        - 1 <= piles.length <= 10^4
        - piles.length <= h <= 10^9
        - 1 <= piles[i] <= 10^9
        """
        # Write your code here
        pass

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    piles1, h1 = [3, 6, 7, 11], 8
    print(f"Test 1: piles = {piles1}, h = {h1}")
    print(f"Output: {solution.minEatingSpeed(piles1, h1)} | Expected: 4\n")

    # Test Case 2
    piles2, h2 = [30, 11, 23, 4, 20], 5
    print(f"Test 2: piles = {piles2}, h = {h2}")
    print(f"Output: {solution.minEatingSpeed(piles2, h2)} | Expected: 30\n")

    # Test Case 3
    piles3, h3 = [30, 11, 23, 4, 20], 6
    print(f"Test 3: piles = {piles3}, h = {h3}")
    print(f"Output: {solution.minEatingSpeed(piles3, h3)} | Expected: 23\n")
